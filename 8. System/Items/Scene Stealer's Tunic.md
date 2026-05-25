---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Comfort]]", "[[Invested]]"]
price: "{'gp': 3000}"
bulk: "L"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of padded armor consists of a beautifully woven pleated tunic adorned with a gold pattern and narrow bands of white fur trim on a deep blue background with matching pants, all of which are meant to signal wealth and status. This +2 resilient raiment padded armor was custom designed for Alessandro Domenesso, an actor as well known for their astounding costume changes as for their roguish off-stage activities. Even without utilizing the magic of this armor, it's elegant enough that it could easily be mistaken as fine clothing.

**Activate—Look At Me!** `pf2:2` (concentrate, illusion, mental, visual)

**Frequency** once per hour

**Effect** You make yourself visible and apparent to a creature you can see that's within 30 feet. The scene stealer's tunic transforms into something incredibly gaudy, distracting, or otherwise compelling to the target creature, who must attempt a DC 30 [[Will]] save.
- **Critical Success** The target is unaffected.
- **Success** The target is distracted by you and keeps looking your way. They take a –1 status penalty to Perception checks against everything but you, a –1 status penalty to all saving throws against your visual effects, and gain a +2 status bonus to all saving throws against visual effects created by anyone else; these penalties and bonus last for 1 minute.
- **Failure** As success, but the target is also [[Off Guard]] to everyone other than you as long as you remain visible.
- **Critical Failure** As failure, but the target also becomes [[Slowed]] 1 as they spend extra time on their turn admiring, glowering, or otherwise being distracted by you.

> [!danger] Effect: Look at Me!

**Source:** `= this.source` (`= this.source-type`)
