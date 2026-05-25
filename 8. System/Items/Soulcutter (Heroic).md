---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Elf]]", "[[Finesse]]", "[[Forceful]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +34; precise low-light vision and hearing within 30 feet

**Communication** telepathy (partner only)

**Skills** Nature +34, Religion +34, Survival +34

**Int** +7, **Wis** +6, **Cha** +5

**Will** +34

The echo of the Calistrian witch Silisifex imbues her legendary blade with a shimmering pale-green glow equivalent to that of candlelight; *Soulcutter* can activate or deactivate this radiance as a free action once per round on her partner's turn. *Soulcutter's* telepathic voice is a sultry whisper that often infuses her observations with a flirtatious edge or a biting sense of dark humor.

*Soulcutter* is a *+3 major striking greater astral holy elven curve blade*. As long as you carry *Soulcutter*, you gain her potency bonus as an item bonus to all saving throws against mental effects. This bonus increases by 2 to +5 against possession effects.

**Activate—Soothe Souls** `pf2:2` (concentrate, healing, manipulate, vitality)

**Frequency** once per hour

**Effect** *Soulcutter* creates a pulse of restorative energy, rejuvenating those within a @Template[type:emanation|distance:30] around you while castigating those in that area who have no place in nature. *Soulcutter* can Sustain this activation for up to 1 minute. Living creatures that start their turn in the area regain 2d8 healing Hit Points, and any fiend or undead creature that starts their turn in the area takes 2d8 spirit damage (DC 38 [[Will]] save).

**Activate—Soulcutting Storm** `pf2:2` (concentrate, manipulate, spirit)

**Frequency** once per hour

**Effect** *Soulcutter* casts a 9th-rank [[Weapon Storm]] to your specification, but all damage caused by the spell is spirit damage. If used to damage a creature that's possessing another creature, this spell does no damage to the possessed creature.

**Activate—Shame Demon** `pf2:2` (concentrate)

**Effect** *Soulcutter* targets a demon she can see or hear within 30 feet, causing the blade's green light to well up around the demon for a moment. The demon suffers the effects of its sin vulnerability, if it has any, and is then temporarily immune to Shame Demon for 24 hours. If *Soulcutter's* partner wasn't aware of the normal effects that trigger that demon's sin vulnerability, they learn it at this time.

**Source:** `= this.source` (`= this.source-type`)
