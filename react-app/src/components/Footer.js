import React from "react";
import { Box, Typography }  from "@mui/material";

function Footer() {
    return (
        <Box sx={{ bgcolor: 'primary.dark', p: 3, mt: 4 }}>
            <Typography variant="body2" color="white" textAlign="center">
                © 2024 Chinese Pronunciation Master
            </Typography>
        </Box>
    )
}

export default Footer;
