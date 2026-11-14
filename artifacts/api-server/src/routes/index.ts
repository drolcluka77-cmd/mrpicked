import { Router, type IRouter } from "express";
import healthRouter from "./health";
import reportRequestsRouter from "./report-requests";
import visitorLanguageRouter from "./visitor-language";

const router: IRouter = Router();

router.use(healthRouter);
router.use(reportRequestsRouter);
router.use(visitorLanguageRouter);

export default router;
