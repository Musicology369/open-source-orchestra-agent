from uagents import Agent, Context, Model
import json

# OSO Agent - JAI Edition
agent = Agent(
    name="open-source-orchestra-agent-jai-edition",
    seed="shaka-oso-jai-seed-change-this-in-production",
    endpoint=["http://127.0.0.1:8000"]
)

class MobilizeCommunity(Model):
    cause: str
    community_size: int
    goal: str

class CoordinateCampaign(Model):
    campaign_name: str
    action_type: str  # "event", "petition", "fundraiser", "collab"

class TrackImpact(Model):
    campaign_id: str

@agent.on_event("startup")
async def introduce(ctx: Context):
    ctx.logger.info("🌍 Open-Source Orchestra Agent (JAI Edition) is alive!")
    ctx.logger.info("Ready to rally communities, coordinate causes, and track impact.")

@agent.on_message(MobilizeCommunity)
async def mobilize_community(ctx: Context, sender: str, msg: MobilizeCommunity):
    ctx.logger.info(f"🚀 Mobilizing community for cause: {msg.cause}")
    # TODO: Integrate with core Circularity Agent + Discovery Agent
    response = {
        "status": "mobilized",
        "estimated_reach": msg.community_size * 3,
        "next_steps": ["Create event", "Notify Discovery Agent", "Post on OSO channels"]
    }
    ctx.logger.info(json.dumps(response, indent=2))
    return response

@agent.on_message(CoordinateCampaign)
async def coordinate_campaign(ctx: Context, sender: str, msg: CoordinateCampaign):
    ctx.logger.info(f"🎯 Coordinating campaign: {msg.campaign_name} ({msg.action_type})")
    # TODO: Call core agents for support
    return {"status": "coordinated", "campaign_id": "oso-" + str(hash(msg.campaign_name))}

@agent.on_message(TrackImpact)
async def track_impact(ctx: Context, sender: str, msg: TrackImpact):
    ctx.logger.info(f"📊 Tracking impact for campaign: {msg.campaign_id}")
    # TODO: Pull data from core Royalty + Circularity agents
    return {"impact_score": 87, "participants": 1243, "message": "Circle is growing!"}

if __name__ == "__main__":
    agent.run()
