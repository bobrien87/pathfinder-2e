---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Herexen"
level: "2"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +6, Deception +7, Religion +10, Stealth +6"
abilityMods: ["+2", "+2", "+1", "+0", "+4", "+3"]
abilities_top:
  - name: "Heretic's Smite"
    desc: "While wielding the favored weapon of its former deity (such as a dagger for an ex-Pharasmin herexen), the herexen's Strikes deal an additional 1d6 spirit damage to creatures with the holy trait."
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "30; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "Final Blasphemy"
    desc: "When the herexen is destroyed, it explodes in a wave of void energy with the effects of a 3-action [[Harm]] spell (DC 18 [[Fortitude]] save). <br>  <br> The herexen is destroyed, so it doesn't gain any Hit Points from this use of *harm*, and it doesn't need to have any *harm* spells remaining to use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, versatile s), **Damage** 1d6 + 4 piercing plus [[Heretics Smite]]"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (4 slots) [[Harm]], [[Harm]], [[Harm]], [[Harm]]"
  - name: "Cleric Domain Spells"
    desc: "DC 18, attack +10<br>**1st** [[Death's Call]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When a cleric rebels against their deity and dies in the grip of blasphemous rage, the heresies they committed in life may fuel their transformation into an undead herexen. Herexens seek vengeance against the deity they once worshipped, defiling temples, slaying the faithful, and rallying lesser undead and death cultists to aid them in their unholy quests. Though a herexen's divine gifts have mostly been corrupted into the vileness of undeath, they stubbornly cling to remnants of their former power, still wielding magic and armaments favored by the deity they so greatly despise.

Groups of herexens that blasphemed against the same deity sometimes combine to form a mockery of a congregation, conducting blasphemous rites with something approaching euphoria. These congregations are often formed from a blasphemous cult whose members practiced their heresy together in life and died together, though some gather independent herexens of the same former faith.

```statblock
creature: "Herexen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
