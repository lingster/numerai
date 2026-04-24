package main

import (
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
)

const endpoint = "https://api-tournament.numer.ai/"

func main() {
	authToken := flag.String("auth", "", "Bearer token for authenticated queries (or set NUMERAI_TOKEN env var)")
	raw := flag.Bool("raw", false, "Output raw JSON without pretty-printing")
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage: query [flags] <graphql-query> [variables-json]\n\n")
		fmt.Fprintf(os.Stderr, "Runs a GraphQL query against %s\n\n", endpoint)
		fmt.Fprintf(os.Stderr, "Arguments:\n")
		fmt.Fprintf(os.Stderr, "  graphql-query   GraphQL query string\n")
		fmt.Fprintf(os.Stderr, "  variables-json  Optional JSON object of query variables\n\n")
		fmt.Fprintf(os.Stderr, "Flags:\n")
		flag.PrintDefaults()
		fmt.Fprintf(os.Stderr, "\nExamples:\n")
		fmt.Fprintf(os.Stderr, "  query '{ rounds(tournament: 8, limit: 1) { number openTime } }'\n")
		fmt.Fprintf(os.Stderr, "  query '{ accountProfile(username: \"alice\", tournament: 8) { models { id displayName } } }'\n")
		fmt.Fprintf(os.Stderr, "  query 'query($id: ID!) { v2RoundModelPerformances(modelId: $id, lastNRounds: 5) { roundNumber corr mmc } }' '{\"id\": \"<model-uuid>\"}'\n")
	}
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		flag.Usage()
		os.Exit(1)
	}

	query := args[0]
	var variables map[string]any
	if len(args) >= 2 {
		if err := json.Unmarshal([]byte(args[1]), &variables); err != nil {
			fmt.Fprintf(os.Stderr, "Error parsing variables JSON: %v\n", err)
			os.Exit(1)
		}
	}

	payload := map[string]any{"query": query}
	if variables != nil {
		payload["variables"] = variables
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error building request: %v\n", err)
		os.Exit(1)
	}

	req, err := http.NewRequest(http.MethodPost, endpoint, bytes.NewReader(body))
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error creating request: %v\n", err)
		os.Exit(1)
	}
	req.Header.Set("Content-Type", "application/json")

	token := *authToken
	if token == "" {
		token = os.Getenv("NUMERAI_TOKEN")
	}
	if token != "" {
		req.Header.Set("Authorization", "Token "+token)
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Request failed: %v\n", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	respBody, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading response: %v\n", err)
		os.Exit(1)
	}

	if *raw {
		os.Stdout.Write(respBody)
		return
	}

	var result any
	if err := json.Unmarshal(respBody, &result); err != nil {
		os.Stdout.Write(respBody)
		return
	}

	pretty, err := json.MarshalIndent(result, "", "  ")
	if err != nil {
		os.Stdout.Write(respBody)
		return
	}
	fmt.Println(string(pretty))

	// Exit non-zero if the response contained GraphQL errors
	if m, ok := result.(map[string]any); ok {
		if errs, ok := m["errors"]; ok && errs != nil {
			os.Exit(2)
		}
	}
}
