---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Artifact]]", "[[Magical]]", "[[Mythic]]", "[[Razing]]", "[[Versatile p]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+4 major striking holy morningstar* is made of wood and adorned with golden flames traced along its haft and head. It has the razing trait, and it ignores the Hardness of structures used to hold those you feel are being unjustly imprisoned (subject to the GM's discretion).

**Activate—Break Free** `pf2:2` (concentrate, manipulate)

**Effect** Spend a Mythic Point; *Freedom's Flame* blazes with a rose-red light, creating a beacon of spiritual strength. Any creature within @Template[emanation|distance:120]{120 feet} that's currently under a compulsion or control effect can immediately attempt a new saving throw to break free of the effect, with a +3 status bonus.

**Activate—Holy Retribution** `pf2:f` (concentrate, divine)

**Trigger** Your previous action was to use *Freedom's Flame* to Strike a foe you have witnessed use a compulsion or control effect on an ally within the past hour

**Frequency** once per day

**Effect** Spend a Mythic Point; your blow is empowered by the righteousness of [[Milani]]. The target's holy weakness is triggered again or, if the target doesn't have a holy weakness, it takes 15 spirit damage.

**Destruction** *Freedom's Flame* is sliced in two if struck by a [[Final Blade]] that has been anointed with [[Unholy Water]] created by a level 20 unholy creature.

**Source:** `= this.source` (`= this.source-type`)
