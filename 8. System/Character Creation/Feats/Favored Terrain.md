---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Ranger]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have studied a specific terrain to overcome its challenges. Choose aquatic, arctic, desert, forest, mountain, plains, sky, swamp, or underground as your favored terrain. When in that terrain, you can ignore the effects of non-magical difficult terrain. If you have the unimpeded journey class feature, you gain a second benefit while in your favored terrain, depending on your choice:

- **Aquatic** You gain a swim Speed equal to your Speed. If you already had a swim Speed, you instead gain a +10-foot status bonus to your swim Speed.

- **Arctic** You need to eat and drink only one-tenth as much as usual, you aren't affected by severe or extreme cold, and you can walk across ice and snow at full Speed without needing to [[Balance]].

- **Desert** You need to eat and drink only one-tenth as much as usual, you aren't affected by severe or extreme heat, and you can walk along sand at full Speed without needing to Balance.

- **Forest, Mountain, or Underground** You gain a climb Speed equal to your Speed. If you already had a climb Speed, you instead gain a +10-foot status bonus to your climb Speed.

- **Plains** You gain a +10-foot status bonus to your land Speed.

- **Sky** You gain a +10-foot status bonus to your fly Speed, if you have one.

- **Swamp** You can move across bogs at full Speed, even if they are deep enough to be greater difficult terrain or to normally require you to Swim.

> [!danger] Effect: Favored Terrain (Gain Climb Speed)

> [!danger] Effect: Favored Terrain (Increase Climb Speed)

> [!danger] Effect: Favored Terrain (Gain Swim Speed)

> [!danger] Effect: Favored Terrain (Increase Swim Speed)

**Source:** `= this.source` (`= this.source-type`)
