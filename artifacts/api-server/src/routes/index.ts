import { Router, type IRouter } from "express";
import healthRouter from "./health";
import reportRequestsRouter from "./report-requests";

const router: IRouter = Router();

router.use(healthRouter);
router.use(reportRequestsRouter);

export default router;
