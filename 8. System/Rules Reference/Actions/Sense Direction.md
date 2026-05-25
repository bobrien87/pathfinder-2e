---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Using the stars, the position of the sun, traits of the geography or flora, or the behavior of fauna, you can stay oriented in the wild. Typically, you attempt a Survival check only once per day, but some environments or changes might necessitate rolling more often. The GM determines the DC and how long this activity takes (usually just a minute or so). More unusual locales or those you're unfamiliar with might require you to have a minimum proficiency rank to Sense Direction. Without a [[Compass]], you take a –2 item penalty to checks to Sense Direction.
- **Critical Success** You get an excellent sense of where you are. If you are in an environment with cardinal directions, you know them exactly.
- **Success** You gain enough orientation to avoid becoming hopelessly lost. If you are in an environment with cardinal directions, you have a sense of those directions.

Sense Direction Tasks- **Untrained** determine a cardinal direction using the sun
- **Trained** find an overgrown path in a forest
- **Expert** navigate a hedge maze
- **Master** navigate a byzantine labyrinth or relatively featureless desert
- **Legendary** navigate an ever-changing dream realm

**Source:** `= this.source` (`= this.source-type`)
