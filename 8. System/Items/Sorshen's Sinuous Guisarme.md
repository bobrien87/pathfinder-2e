---
type: item
source-type: "Remaster"
level: "23"
traits: ["[[Artifact]]", "[[Intelligent]]", "[[Magical]]", "[[Mythic]]", "[[Reach]]", "[[Trip]]"]
price: "{'cp': 0, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +37; precise vision 300 feet, imprecise hearing 300 feet, darkvision

**Communication** telepathy (Aklo, Azlanti, Chthonian, and Thassilonian)

**Skills** Arcana +43, Occultism +38, Society +36

**Int** +6, **Wis** +6, **Cha** +8

**Will** +37

*Sorshen's Sinuous Guisarme* is a *+4 mythic striking keen quickstrike shifting spell reservoir high-grade dawnsilver guisarme*. The weapon's unique double-bladed design combined with her magical nature grants her the twin weapon trait. Her spell reservoir rune typically contains blindness. Her power and intelligence are derived from a magical gemstone containing 13 of Sorshen's dreams, all so outlandish or salacious that most would consider them to be nightmares—although these dreams have been transforming into less horrific visions as Sorshen's changing philosophies continue to influence her weapon. The guisarme can use 3 actions per turn, acting on her wielder's turn. These actions don't count against her wielder's.

**Activate—Arcane Shift** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You activate the guisarme's shifting rune to Shift Weapon

**Effect** The guisarme transforms into a [[Staff of Control (Major)]] with 10 charges. If you spend 1 Mythic Point when you Cast a Spell from this staff and expend 10 charges, the spell is heightened to 10th rank, and its save DC and attack rolls are calculated at mythic proficiency. While in major staff of control form, none of the guisarme's weapon runes are active, nor can she Impose Will, but she remains a high-grade dawnsilver item and retains her intelligence—she can use her actions to Cast a Spell from the staff but can't spend Mythic Points to heighten spells to 10th rank. She automatically reverts to guisarme form once all her charges are expended or if you command the staff to revert to guisarme form by using Shift Weapon again.

**Activate—Impose Will** `pf2:2` Cast a Spell

**Frequency** once per day per spell

**Effect** *Sorshen's Sinuous Guisarme* casts one of the following spells, heightened to 10th rank, to your specifications: [[Charm]] (DC 45), [[Flicker]], or [[Subconscious Suggestion]] (DC 45). The guisarme can use this activation. If you use this activation and spend 1 Mythic Point, the save DC for the spell increases to DC 50.

**Destruction** *Sorshen's Sinuous Guisarme* can be destroyed if it's hurled under the crushing feet of the Oliphaunt of Jandelay, but only if there's no current runelord of lust living in the world. Note that when Sorshen took on the mantle of ruler of New Thassilon, she abandoned her role as runelord of lust, so at this time, half of this destruction requirement is already fulfilled. Of course, a PC who decides to toss this weapon under the Oliphaunt's feet during the course of this adventure will likely disappoint—or perhaps even enrage—Queen Sorshen, who might seek retaliation in the future.

**Source:** `= this.source` (`= this.source-type`)
