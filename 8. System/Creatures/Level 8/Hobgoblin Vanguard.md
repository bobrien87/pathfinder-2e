---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin Vanguard"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Athletics +18, Crafting +17, Intimidation +16, Survival +16"
abilityMods: ["+5", "+2", "+3", "+2", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +13, **Will** +16"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "Shock and Awe"
    desc: "`pf2:r` **Trigger** The hobgoblin vanguard critically hits a creature with an alchemical grenade Strike <br>  <br> **Effect** The hobgoblin vanguard attempts to `act demoralize` the creature with a mere look. If the target creature was reduced to 0 Hit Points by the triggering Strike, the hobgoblin vanguard can instead attempt to Demoralize all opponents within 30 feet, rolling once and comparing the result to each target's Will DC."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Maul +19 (`pf2:1`) (magical, shove), **Damage** 2d12+8 bludgeoning plus [[Knockdown]]"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Alchemical Grenade +16 (`pf2:1`) (splash, range 20 ft.), **Damage** 2 acid plus 2d8 acid plus 2 acid"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Though there are times for precision and discipline, every hobgoblin general also understands the value of demoralizing the enemy with a show of overwhelming force. No military unit is better suited to this purpose than the vanguard, a heavily armed and armored elite unit that inspires their fellow soldiers to action while breaking the enemy's lines and morale with terrifying explosive weapons.

Hobgoblins are respected across Golarion for their unmatched expertise in the art of war. The recent foundation of the hobgoblin nation of Oprak and its unprecedented acts of diplomacy, including non-aggression pacts with the neighboring nations of Nidal and Nirmathas, has given some hope that a lasting peace might finally be established; however, there remains no shortage of unaffiliated hobgoblin raiders and pillagers.

```statblock
creature: "Hobgoblin Vanguard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
