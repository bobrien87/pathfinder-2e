---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wealthy Vigilante"
level: "8"
rare_01: "Rare"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +16, Deception +17, Intimidation +17, Society +16, Stealth +17"
abilityMods: ["+4", "+2", "+1", "+3", "+1", "+3"]
abilities_top:
  - name: "Custom Gear"
    desc: "The wealthy vigilante's support team has spent years tailoring and tuning the vigilante's equipment. Anyone but the vigilante attempting to use the items takes the same drawbacks they would if they were shoddy items. These peculiarities make the items have no value if sold."
  - name: "Talisman Prepper"
    desc: "The vigilante goes on patrol with six talismans of 6th level or lower. The typical set includes a [[Fear Gem]] and [[Emerald Grasshopper]] affixed, with a [[Dragon Turtle Scale]], [[Effervescent Ampoule]], [[Feather Step Stone]], and [[Iron Cube]] in storage."
armorclass:
  - name: AC
    desc: "27; **Fort** +12, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Quick Replace"
    desc: "`pf2:r` **Trigger** The wealthy vigilante Activates one of their affixed talismans <br>  <br> **Requirements** The wealthy vigilante has a hand free <br>  <br> **Effect** As soon as one of their talismans burns out, the wealthy vigilante pulls another from their crimefighting pouches and deftly [[Affixes]] it to replace the used talisman."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +19 (`pf2:1`) (magical, versatile p), **Damage** 2d8+10 slashing"
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Flintlock Musket +17 (`pf2:1`) (concussive, fatal d10, magical, reload 1, range 70 ft.), **Damage** 2d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Calculated Strike"
    desc: "`pf2:2` The wealthy vigilante makes a melee Strike. If the Strike hits, the vigilante can then `act shove` the target. This Shove uses the same multiple attack penalty as the Strike and doesn't count toward the vigilante's multiple attack penalty, but the vigilante must Stride after the pushed creature. If the Strike misses, the vigilante can Step up to three times, each of which must take it further from the target. The vigilante can `act hide` if, after the Steps, they have cover or concealment from the target."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

By night, this member of the nobility dons a false identity to mete out violent, extralegal justice on petty criminals and the downtrodden. They're possessed of unwavering self-righteousness and the best equipment money can buy.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Wealthy Vigilante"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
