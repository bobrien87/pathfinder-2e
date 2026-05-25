---
type: creature
group: ["Gnome", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Umbral Gnome Warrior"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Gnomish, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +5, Stealth +5"
abilityMods: ["+4", "+2", "+3", "+0", "+1", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18 (20 with shield raised); **Fort** +9, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "34"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +10 (`pf2:1`), **Damage** 1d6+4 piercing"
  - name: "Ranged strike"
    desc: "Heavy Crossbow +8 (`pf2:1`) (reload 2, range 120 ft.), **Damage** 1d10 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 15, attack +7<br>**1st** [[Illusory Disguise]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Umbral gnome warriors are quick to charge into battle but focus on defending their kin and their homes over more aggressive tactics when a choice is available.

Gnomes are known for being creative and curious. They stand at around 3 feet tall, and their vivid personalities match their naturally vivid hair and eye color. Gnomes possess a natural connection to their ancestral home, the First World. They crave adventure and new experiences to fight off an ancestry-wide affliction known as the Bleaching. Gnomes who fail to dream and innovate begin to slowly lose their color and fall into a deep depression.

A notable subgroup of gnomes called umbral gnomes typically have gray or brown skin with a stony texture, and thin, pale hair or bald pates. Umbral gnomes are most numerous in the Darklands, where they go by the name drathnelar. Umbral gnomes often attribute these physical changes to the gnome deity regarded as the first of their kind, Nivi Rhombodazzle. Nivi was a surface gnome who traveled deep into the Darklands and was ultimately rewarded with demigodhood when she exchanged a particular gemstone with the dwarven deity, Torag. Nivi is immune to the Bleaching, and umbral gnomes are often immune or resistant to it as well.

```statblock
creature: "Umbral Gnome Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
