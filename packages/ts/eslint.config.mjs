import js from "@eslint/js";
import tsParser from "@typescript-eslint/parser";
import tsPlugin from "@typescript-eslint/eslint-plugin";

export default [
  // Optional: baseline JS recommended rules (safe even for TS projects)
  js.configs.recommended,

  {
    files: ["src/**/*.ts"],
    languageOptions: {
      parser: tsParser, // ✅ THIS IS THE KEY
      parserOptions: {
        ecmaVersion: 2022,
        sourceType: "module",
        // If you want type-aware rules later, uncomment:
        // project: "./tsconfig.json",
        // tsconfigRootDir: import.meta.dirname,
      },
    },
    plugins: {
      "@typescript-eslint": tsPlugin,
    },
    rules: {
      // Turn off base rule, use TS-aware version if you want
      "no-unused-vars": "off",
      "@typescript-eslint/no-unused-vars": "off",
    },
  },
];
