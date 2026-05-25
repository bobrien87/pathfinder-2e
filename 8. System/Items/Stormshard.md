---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These shards of coalesced necromantic essence are sometimes found in the wake of an ancestor storm. Howling spirits are faintly visible, trapped inside the jagged, dark-green glass.

You can use the shard to cow the undead or briefly release the tormented souls from inside the glass. While you hold the stormshard, you gain a +1 item bonus to Intimidation checks to influence the undead. In addition, you can [[Demoralize]] undead creatures, even if those creatures are mindless or otherwise immune to emotion, fear, or mental effects.

**Activate—Free the Spirits** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You briefly release the spirits from the *stormshard* before drawing them back into the glass. Each creature in a @Template[type:emanation|distance:10] takes 4d8 void damage (DC 20 [[Fortitude]] save). You treat the result of your saving throw as one degree of success better than its outcome.

**Source:** `= this.source` (`= this.source-type`)
