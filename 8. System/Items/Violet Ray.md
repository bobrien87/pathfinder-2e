---
type: item
source-type: "Remaster"
level: "12"
price: "{'gp': 1893}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

One of the many wondrous devices brought into the world by Stasian technology is the seemingly miraculous violet ray. Physicians claim it anything from headaches to heartburn, or nausea to deafness, all with an easy and painless treatment. The device is a glass vacuum with an insulated handle connected to a small Stasian coil. When powered, the glass tube fills with purple light and becomes warm to the touch. Pressing the tube to one's body is said to increase blood flow, eliminate toxins, and many other beneficial effects. A violet ray functions as a [[Healer's Toolkit]] and provides a +2 item bonus to Medicine checks to [[Administer First Aid]], [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]].

**Activate—Electric Love** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** You apply the violet ray to an adjacent creature and attempt to counteract the [[Blinded]], [[Clumsy]], [[Confused]], [[Deafened]], [[Drained]], [[Enfeebled]], [[Sickened]], or [[Stupefied]] condition with a counteract rank of 6 and a counteract modifier of +22, using the source of the condition to determine the condition's counteract rank and DC. If the condition was caused by an ongoing effect and you don't remove that effect, the condition returns after 1 minute. Each use of this ability can only counteract a single condition.

**Source:** `= this.source` (`= this.source-type`)
