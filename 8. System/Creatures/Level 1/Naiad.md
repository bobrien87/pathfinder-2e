---
type: creature
group: ["Amphibious", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Naiad"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: "Water"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +3, Diplomacy +7, Nature +6, Stealth +6, Survival +4"
abilityMods: ["+0", "+3", "+0", "+1", "+1", "+4"]
abilities_top:
  - name: "Animal Empathy"
    desc: "The naiad can ask questions of, receive answers from, and use the Diplomacy skill with animals."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Water Healing"
    desc: "For every 10 minutes a naiad spends soaking in her bonded body of water, she regains 7 Hit Points."
armorclass:
  - name: AC
    desc: "14; **Fort** +3, **Ref** +6, **Will** +8"
health:
  - name: HP
    desc: "20; **Weaknesses** cold iron 3; **Resistances** fire 3"
abilities_mid:
  - name: "Water Dependent"
    desc: "A naiad is bonded to a spring, pond, or similar-sized water feature. If she is more than 300 feet away from it for 24 hours or more, she gains the weak adjustments until she returns. She can perform a 24-hour ritual to bond herself to a new body of water."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Aqueous Fist +8 (`pf2:1`) (agile, finesse, magical, water), **Damage** 1d8 bludgeoning"
  - name: "Ranged strike"
    desc: "Water Orb +8 (`pf2:1`) (magical, water), **Damage** 1d6 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +9<br>**1st** [[Charm]], [[Create Water]], [[Hydraulic Push]], [[Tidal Surge]] (At Will)"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Naiads protect streams, ponds, springs, and other natural bodies of fresh water. While most naiads lead solitary lives close to their chosen home, sometimes they congregate in coven-like groups where river tributaries meet, performing great magic and blessing the waters of the land. Because naiads' bonds to their bodies of water permit more flexibility, they are the nymphs most likely to interact with humanoids—and even visit their settlements on occasion. Unlike other nymphs, naiads occasionally become adventurers, especially when dark forces seek to despoil nature or otherwise threaten the land, joining forces with others to prevent the corruption of the natural world.

Nymphs are a family of fey that take the form of beautiful humanoids with elven features and have a deep association with the natural world. The most common of their kind are the dryads, which are spirits that embody great trees, but many other kinds of nymphs exist, including naiads, who watch over bodies of water. All nymphs are guardians of some element of nature, typically a specific tree or pond, or even-in the case of nymph queens-whole forests or massive bodies of water

```statblock
creature: "Naiad"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
