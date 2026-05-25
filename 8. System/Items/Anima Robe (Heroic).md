---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Illusion]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +33; precise low-light vision and hearing within 30 feet

**Communication** telepathy (partner only)

**Skills** Deception +35, Occultism +34, Performance +35

**Int** +6, **Wis** +5, **Cha** +7

**Will** +33

The artistic echo of the Ekujae hero Iyalirrin animates the *Anima Robe's* stitching to display embroidered reactions to situations experienced by the wearer. The *Anima Robe's* telepathic voice is filled with confidence (almost to the point of cockiness) and is supportive, often encouraging his partner to take risky or showy actions yet never to the extent that would put them in significant harm's way.

The *Anima Robe* grants a +3 item bonus to Diplomacy checks made to [[Make an Impression]] and to all Performance checks, and you gain resistance 15 to mental damage.

**Activate–Billowing Distraction** `pf2:2` (concentrate)

**Effect** The *Anima Robe* billows as if in a blustery wind and attempts to [[Feint]] a creature you're adjacent to.

**Activate–Who Am I?** `pf2:2` (concentrate)

**Effect** The robe's hood rises up over your head, casting a 4th-rank [[Illusory Disguise]] to your specifications.

**Activate–Who Are We?** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** The robe's hem swishes, casting a 7th-rank *illusory disguise* to your specifications.

**Activate—Who Are They?** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** An image of a creature shows up in the robe's stitching, then appears to come to life; the robe casts an 8th-rank [[Illusory Creature]] to your specifications. The robe can use an action to Sustain this activation for up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
