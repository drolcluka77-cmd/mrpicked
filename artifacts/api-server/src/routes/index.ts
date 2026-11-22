import { Router, type IRouter } from "express";
import healthRouter from "./health";
import reportRequestsRouter from "./report-requests";
import mediaRouter from "./media";

const router: IRouter = Router();

router.use(healthRouter);
router.use(reportRequestsRouter);
router.use(mediaRouter);

export default router;
