---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Envoy"
level: "0"
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
    desc: "+7"
languages: "Common (plus two additional languages)"
skills:
  - name: Skills
    desc: "Deception +13, Diplomacy +15, Intimidation +7, Society +15"
abilityMods: ["+0", "+1", "+0", "+4", "+3", "+3"]
abilities_top:
  - name: "+6 to Sense Motive"
    desc: ""
  - name: "Diplomatic Specialist"
    desc: "When dealing with matters of statecraft and negotiation, the envoy is a 6th-level challenge."
armorclass:
  - name: AC
    desc: "13; **Fort** +2, **Ref** +3, **Will** +11"
health:
  - name: HP
    desc: "12"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +5 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +5 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Diplomatic Immunity"
    desc: "`pf2:1` The envoy invokes their diplomatic status. Until the end of the envoy's next turn, any creature that attempts to attack them must succeed at a DC 15 [[Will]] save or have their attack disrupted. The attacker gains weakness 2 to all damage from the envoy's allies while Diplomatic Immunity lasts, whether their attack was disrupted or not. <br>  <br> > [!danger] Effect: Diplomatic Immunity"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Envoys are guests of a given court, representing the interests of another court or organization. Some envoys stay in one place so long they're practically considered locals, though those with whom they parley are swiftly reminded where their loyalty lies.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Envoy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
