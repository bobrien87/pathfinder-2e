---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Divine]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +35; precise low-light vision and hearing within 30 feet

**Communication** telepathy (partner only)

**Skills** Demon Lore +33, Diplomacy +34, Religion +35

**Int** +5, **Wis** +7, **Cha** +6

**Will** +35

The stately echo of Jininsiel, the woman who guided her people through the Darklands to escape the devastation of Earthfall, causes *Fiendbreaker* to softly shimmer with a silvery radiance equivalent to that of candlelight. *Fiendbreaker* can activate or deactivate this radiance as a free action once per round on her partner's turn. *Fiendbreaker's* telepathic voice is calm and soothing, seeking to support her partner's decisions with compliments or warnings against overconfidence as needed.

*Fiendbreaker* functions as a *+3 major striking holy high-grade cold iron staff*. While wielding the staff, you gain a +3 circumstance bonus to checks to [[Recall Knowledge]] about any sort of fiend.

**Activate** Cast a Spell

**Frequency** once per round

**Effect** You expend a number of charges from the staff to cast a spell from her list. *Fiendbreaker* can use this activation only if you're holding the staff and only if you haven't used *Fiendbreaker* to Cast a Spell this round. Likewise, if *Fiendbreaker* Casts a Spell from the staff, you can't activate the staff to Cast a Spell this round.

- **Cantrip** [[Divine Lance]]
- **1st** [[Sanctuary]]
- **2nd** [[See the Unseen]]
- **3rd** [[Anointed Ground]], [[Holy Light]]
- **4th** [[Clear Mind]], [[Planar Tether]]
- **5th** [[Banishment]], [[Divine Wrath]]
- **6th** [[Holy Light]], [[Spirit Blast]]
- **7th** [[Divine Decree]], [[Planar Seal]]
- **8th** [[Divine Wrath]], [[Holy Light]]
- **9th** [[Banishment]], [[Divine Decree]]

**Activate—Restore Mind** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** *Fiendbreaker* attempts to counteract an ongoing mental affect you're suffering from, with a counteract rank of 9th and a +25 modifier to the roll (or a +30 modifier if the source of the mental effect on you was created by a fiend).

**Source:** `= this.source` (`= this.source-type`)
