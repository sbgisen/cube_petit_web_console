import { Container, Paper, Typography, Button, Stack } from "@mui/material";

export default function App() {
  return (
    <Container maxWidth="sm" sx={{ py: 6 }}>
      <Paper sx={{ p: 4, borderRadius: 4 }}>
        <Typography variant="h4" fontWeight="bold">
          Cube petit Web Console
        </Typography>

        <Typography sx={{ mt: 1 }} color="text.secondary">
          Vite + React + TypeScript + MUI
        </Typography>

        <Stack direction="row" spacing={2} sx={{ mt: 3 }}>
          <Button variant="contained">Connect</Button>
          <Button variant="outlined">Disconnect</Button>
        </Stack>
      </Paper>
    </Container>
  );
}
