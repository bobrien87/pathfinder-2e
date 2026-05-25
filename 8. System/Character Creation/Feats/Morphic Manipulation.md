---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Exploration]]", "[[General]]", "[[Primal]]", "[[Skill]]", "[[Vitality]]"]
prerequisites: "master in Nature"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've attuned your natural aura to that of plant life, coaxing it to grow faster than normal. You sit for 10 minutes with a small, natural non-creature plant—such as a lone flower, a small bush, or a potted succulent—while you bring your aura in tune through meditation. You coax the plant to advance one stage in its life cycle: from seed to sprout, sprout to plant, plant to flower, or flower to fruit. If the plant doesn't have proper nutrients (if you're sprouting a seed without soil or water, for example), the plant withers 5 minutes after you complete the activity. Performing this activity more than once per day renders you [[Fatigued]] and unable to use Morphic Manipulation until your next full night's rest.

**Source:** `= this.source` (`= this.source-type`)
