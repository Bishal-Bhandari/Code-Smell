import { motion } from "framer-motion";

export default function Card({ children }) {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="bg-white/5 backdrop-blur-lg border border-white/10 rounded-2xl p-6 shadow-lg"
    >
      {children}
    </motion.div>
  );
}