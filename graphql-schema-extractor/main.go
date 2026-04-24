package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"sort"
	"strings"
)

const endpoint = "https://api-tournament.numer.ai/"

const introspectionQuery = `
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type { ...TypeRef }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
`

type introspectionResponse struct {
	Data struct {
		Schema introspectionSchema `json:"__schema"`
	} `json:"data"`
	Errors []struct {
		Message string `json:"message"`
	} `json:"errors"`
}

type introspectionSchema struct {
	QueryType        *typeRef        `json:"queryType"`
	MutationType     *typeRef        `json:"mutationType"`
	SubscriptionType *typeRef        `json:"subscriptionType"`
	Types            []fullType      `json:"types"`
	Directives       []directiveDef  `json:"directives"`
}

type typeRef struct {
	Name   string   `json:"name"`
	Kind   string   `json:"kind"`
	OfType *typeRef `json:"ofType"`
}

type fullType struct {
	Kind          string       `json:"kind"`
	Name          string       `json:"name"`
	Description   string       `json:"description"`
	Fields        []fieldDef   `json:"fields"`
	InputFields   []inputValue `json:"inputFields"`
	Interfaces    []typeRef    `json:"interfaces"`
	EnumValues    []enumValue  `json:"enumValues"`
	PossibleTypes []typeRef    `json:"possibleTypes"`
}

type fieldDef struct {
	Name              string       `json:"name"`
	Description       string       `json:"description"`
	Args              []inputValue `json:"args"`
	Type              typeRef      `json:"type"`
	IsDeprecated      bool         `json:"isDeprecated"`
	DeprecationReason string       `json:"deprecationReason"`
}

type inputValue struct {
	Name         string  `json:"name"`
	Description  string  `json:"description"`
	Type         typeRef `json:"type"`
	DefaultValue *string `json:"defaultValue"`
}

type enumValue struct {
	Name              string `json:"name"`
	Description       string `json:"description"`
	IsDeprecated      bool   `json:"isDeprecated"`
	DeprecationReason string `json:"deprecationReason"`
}

type directiveDef struct {
	Name        string       `json:"name"`
	Description string       `json:"description"`
	Locations   []string     `json:"locations"`
	Args        []inputValue `json:"args"`
}

func fetchSchema() (*introspectionSchema, error) {
	body, err := json.Marshal(map[string]string{"query": introspectionQuery})
	if err != nil {
		return nil, err
	}

	resp, err := http.Post(endpoint, "application/json", bytes.NewReader(body))
	if err != nil {
		return nil, fmt.Errorf("request failed: %w", err)
	}
	defer resp.Body.Close()

	raw, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("reading response: %w", err)
	}

	var result introspectionResponse
	if err := json.Unmarshal(raw, &result); err != nil {
		return nil, fmt.Errorf("parsing response: %w", err)
	}

	if len(result.Errors) > 0 {
		msgs := make([]string, len(result.Errors))
		for i, e := range result.Errors {
			msgs[i] = e.Message
		}
		return nil, fmt.Errorf("graphql errors: %s", strings.Join(msgs, "; "))
	}

	return &result.Data.Schema, nil
}

func typeRefToSDL(t typeRef) string {
	if t.Kind == "NON_NULL" {
		if t.OfType != nil {
			return typeRefToSDL(*t.OfType) + "!"
		}
	}
	if t.Kind == "LIST" {
		if t.OfType != nil {
			return "[" + typeRefToSDL(*t.OfType) + "]"
		}
	}
	return t.Name
}

func descriptionBlock(desc, indent string) string {
	if desc == "" {
		return ""
	}
	escaped := strings.ReplaceAll(desc, `"""`, `\"""`)
	if !strings.Contains(escaped, "\n") {
		return fmt.Sprintf("%s\"\"\"%s\"\"\"\n", indent, escaped)
	}
	return fmt.Sprintf("%s\"\"\"\n%s%s\n%s\"\"\"\n", indent, indent, escaped, indent)
}

func renderInputValue(iv inputValue) string {
	s := fmt.Sprintf("%s: %s", iv.Name, typeRefToSDL(iv.Type))
	if iv.DefaultValue != nil && *iv.DefaultValue != "" {
		s += " = " + *iv.DefaultValue
	}
	return s
}

func renderArgs(args []inputValue) string {
	if len(args) == 0 {
		return ""
	}
	parts := make([]string, len(args))
	for i, a := range args {
		parts[i] = renderInputValue(a)
	}
	if len(parts) == 1 {
		return "(" + parts[0] + ")"
	}
	return "(\n    " + strings.Join(parts, "\n    ") + "\n  )"
}

func renderType(t fullType) string {
	var sb strings.Builder

	sb.WriteString(descriptionBlock(t.Description, ""))

	switch t.Kind {
	case "OBJECT":
		ifaces := make([]string, len(t.Interfaces))
		for i, iface := range t.Interfaces {
			ifaces[i] = iface.Name
		}
		impl := ""
		if len(ifaces) > 0 {
			impl = " implements " + strings.Join(ifaces, " & ")
		}
		sb.WriteString(fmt.Sprintf("type %s%s {\n", t.Name, impl))
		for _, f := range t.Fields {
			sb.WriteString(descriptionBlock(f.Description, "  "))
			deprecated := ""
			if f.IsDeprecated {
				reason := f.DeprecationReason
				if reason == "" {
					reason = "No longer supported"
				}
				deprecated = fmt.Sprintf(` @deprecated(reason: "%s")`, reason)
			}
			sb.WriteString(fmt.Sprintf("  %s%s: %s%s\n", f.Name, renderArgs(f.Args), typeRefToSDL(f.Type), deprecated))
		}
		sb.WriteString("}\n")

	case "INPUT_OBJECT":
		sb.WriteString(fmt.Sprintf("input %s {\n", t.Name))
		for _, f := range t.InputFields {
			sb.WriteString(descriptionBlock(f.Description, "  "))
			sb.WriteString(fmt.Sprintf("  %s\n", renderInputValue(f)))
		}
		sb.WriteString("}\n")

	case "INTERFACE":
		sb.WriteString(fmt.Sprintf("interface %s {\n", t.Name))
		for _, f := range t.Fields {
			sb.WriteString(descriptionBlock(f.Description, "  "))
			sb.WriteString(fmt.Sprintf("  %s%s: %s\n", f.Name, renderArgs(f.Args), typeRefToSDL(f.Type)))
		}
		sb.WriteString("}\n")

	case "UNION":
		types := make([]string, len(t.PossibleTypes))
		for i, pt := range t.PossibleTypes {
			types[i] = pt.Name
		}
		sb.WriteString(fmt.Sprintf("union %s = %s\n", t.Name, strings.Join(types, " | ")))

	case "ENUM":
		sb.WriteString(fmt.Sprintf("enum %s {\n", t.Name))
		for _, ev := range t.EnumValues {
			sb.WriteString(descriptionBlock(ev.Description, "  "))
			deprecated := ""
			if ev.IsDeprecated {
				reason := ev.DeprecationReason
				if reason == "" {
					reason = "No longer supported"
				}
				deprecated = fmt.Sprintf(` @deprecated(reason: "%s")`, reason)
			}
			sb.WriteString(fmt.Sprintf("  %s%s\n", ev.Name, deprecated))
		}
		sb.WriteString("}\n")

	case "SCALAR":
		sb.WriteString(fmt.Sprintf("scalar %s\n", t.Name))
	}

	return sb.String()
}

func renderSchema(schema *introspectionSchema) string {
	var sb strings.Builder

	// schema block
	hasNonDefault := false
	if schema.QueryType != nil && schema.QueryType.Name != "Query" {
		hasNonDefault = true
	}
	if schema.MutationType != nil && schema.MutationType.Name != "Mutation" {
		hasNonDefault = true
	}
	if schema.SubscriptionType != nil && schema.SubscriptionType.Name != "Subscription" {
		hasNonDefault = true
	}
	if hasNonDefault {
		sb.WriteString("schema {\n")
		if schema.QueryType != nil {
			sb.WriteString(fmt.Sprintf("  query: %s\n", schema.QueryType.Name))
		}
		if schema.MutationType != nil {
			sb.WriteString(fmt.Sprintf("  mutation: %s\n", schema.MutationType.Name))
		}
		if schema.SubscriptionType != nil {
			sb.WriteString(fmt.Sprintf("  subscription: %s\n", schema.SubscriptionType.Name))
		}
		sb.WriteString("}\n\n")
	}

	// directives
	builtinDirectives := map[string]bool{"skip": true, "include": true, "deprecated": true, "specifiedBy": true}
	for _, d := range schema.Directives {
		if builtinDirectives[d.Name] {
			continue
		}
		sb.WriteString(descriptionBlock(d.Description, ""))
		args := renderArgs(d.Args)
		locs := strings.Join(d.Locations, " | ")
		sb.WriteString(fmt.Sprintf("directive @%s%s on %s\n\n", d.Name, args, locs))
	}

	// group types by kind
	kindOrder := []string{"SCALAR", "ENUM", "INTERFACE", "UNION", "INPUT_OBJECT", "OBJECT"}
	byKind := make(map[string][]fullType)
	for _, t := range schema.Types {
		if strings.HasPrefix(t.Name, "__") {
			continue
		}
		byKind[t.Kind] = append(byKind[t.Kind], t)
	}
	for _, kind := range kindOrder {
		types := byKind[kind]
		sort.Slice(types, func(i, j int) bool { return types[i].Name < types[j].Name })
		for _, t := range types {
			sb.WriteString(renderType(t))
			sb.WriteString("\n")
		}
	}

	return sb.String()
}

func main() {
	fmt.Fprintln(os.Stderr, "Fetching GraphQL schema from", endpoint)

	schema, err := fetchSchema()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	sdl := renderSchema(schema)
	fmt.Print(sdl)

	fmt.Fprintf(os.Stderr, "Done. Types: %d, Directives: %d\n", len(schema.Types), len(schema.Directives))
}
