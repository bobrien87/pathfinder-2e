---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 450}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved in a putrid jade, the color of disease, this figurine is a bloated humanoid mass of writhing vermin and serpents, all rendered in disgusting detail. The creeping pattern is carved so they seem to move and contort the more one views the figurine. When activated, the effect is amplified to a disgusting or horrifying degree. The figurine can be activated twice per day. If you try to activate it a third time during a day, it dissolves into a puddle of non-magical, putrid glue, causing you to become [[Sickened]] 3.

**Activate** `pf2:2` (concentrate, manipulate)

**Effect** Holding the figurine over your head and speaking one command word causes a wave of nausea in a @Template[type:emanation|distance:20]. Each creature in the emanation must succeed at a DC 24 [[Fortitude]] save or become [[Sickened]] 2. You're immune to this effect.

**Activate** `pf2:2` (concentrate, manipulate)

**Effect** Holding the figurine over your head and speaking a different command word causes those around to tremble in fear. Each creature in a @Template[type:emanation|distance:20] must succeed at a DC 24 [[Will]] save or become [[Frightened]] 3. You're immune to this effect.

**Source:** `= this.source` (`= this.source-type`)
