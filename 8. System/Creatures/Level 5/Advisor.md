---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Advisor"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +14, Diplomacy +14, Occultism +10, Performance +12, Society +12, Legal Lore +12"
abilityMods: ["+0", "+2", "-1", "+3", "+3", "+5"]
abilities_top:
  - name: "Placate"
    desc: "An advisor is well versed in soothing agitated nobles. Their claming voice gives them a +2 circumstance bonus to Deception and Diplomacy checks when dealing with members of the nobility."
armorclass:
  - name: AC
    desc: "21; **Fort** +8, **Ref** +11, **Will** +14"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Whip +11 (`pf2:1`) (disarm, finesse, nonlethal, reach 10 ft., trip), **Damage** 1d4+4 slashing"
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14<br>**3rd** (2 slots) [[Mind Reading]], [[Ring of Truth]]<br>**2nd** (3 slots) [[Augury]], [[Cleanse Affliction]], [[Stupefy]]<br>**1st** (3 slots) [[Command]], [[Daze]], [[Force Barrage]], [[Light]], [[Prestidigitation]], [[Protection]], [[Shield]], [[Soothe]], [[Void Warp]]"
  - name: "Bard Composition Spells"
    desc: "DC 22, attack +14<br>**2nd** [[Rallying Anthem]]<br>**1st** [[Counter Performance]], [[Courageous Anthem]], [[Uplifting Overture]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Trusted counselors of the court, advisors whisper words of guidance into the ears of those in power. Many nobles lean so heavily on their advisor's counsel that they make few decisions without them and insist on their attendance at all meetings and public events. Advisors are often master manipulators.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Advisor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
