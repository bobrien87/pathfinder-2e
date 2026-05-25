---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Emotion]]", "[[Magical]]", "[[Wood]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Named because of its popularity among thieves to distract any authorities in pursuit, a *captivating rosebud* has a near-irresistible fragrance.

**Activate - Scent of Roses** `pf2:1` (manipulate, mental, olfactory)

**Effect** You throw the captivating rosebud in a square adjacent to you. The rosebud quickly sprouts into a little rosebush that lasts for 1 hour. Any creature that passes within 15 feet of the rose bush, other than yourself, must attempt a DC 18 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –1 status penalty to Perception checks for 10 minutes.
- **Failure** As success, but a –2 penalty.
- **Critical Failure** As success, but a –2 penalty and the creature is [[Fascinated]] by the rosebush.

**Activate - Rose Vines** 10 minutes (manipulate)

**Effect** You plant the captivating rosebud into a square adjacent to a building or other structure. It grows into a rosebush that stretches up to 30 feet tall. You and your allies can use the rosebush as a ladder to Climb easily up and down the side of the adjacent structure, but all other creatures must succeed at a DC 17 [[Will]] save saving throw or fail to notice the rosebush's presence.

**Source:** `= this.source` (`= this.source-type`)
