---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *Liver Bloodstone of Arazni* represents confidence. While holding the Liver Bloodstone, you feel more certain in your abilities.

**Activate—Embolden**`pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You critically succeed on an attack roll, saving throw, or skill check while in encounter mode

**Effect** You gain temporary Hit Points equal to your level for 1 round.

> [!danger] Effect: Embolden

**Activate—Arazni's Fervor** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You worship Arazni or are favored by her

**Effect** You hold the Liver Bloodstone aloft, and the Bloodstone glows with crimson light, filling you and your allies with Arazni's wrath. The Liver Bloodstone casts [[Bless]]. For the next minute, you can use a free action at the beginning of each of your turns to increase the spell's emanation radius by 10 feet. You can't increase the emanation's radius in any other way.

**Destruction** The Liver Bloodstone melts into a puddle of poison if a worshipper of Arazni willingly submerges the Bloodstone in a lethal contact or consumed poison, then licks the Bloodstone clean. Each creature in a @Template[type:emanation|distance:15] is exposed to the poison that destroyed the *Bloodstone*, as if they'd touched or consumed that poison.

**Source:** `= this.source` (`= this.source-type`)
