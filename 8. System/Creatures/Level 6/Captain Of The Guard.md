---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Captain Of The Guard"
level: "6"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +15, Diplomacy +11, Intimidation +13, Society +10, Legal Lore +12, Warfare Lore +8"
abilityMods: ["+5", "+0", "+2", "+0", "+3", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24 (26 with shield raised); **Fort** +14, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "Aura of Command"
    desc: "30 feet. The captain of the guard bolsters lower-level guards under their command, granting them a +1 status bonus to their attack rolls and a +2 status bonus to their Will saves. <br>  <br> > [!danger] Effect: Under Command <br>  <br> > [!danger] Effect: Aura of Command"
  - name: "Bravery"
    desc: "When the captain of the guard rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the [[Frightened]] condition, reduce its value by 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
  - name: "Shield Warden"
    desc: "When the captain has their shield raised, they can [[Shield Block]] when an attack is made against an adjacent ally. If they do, the shield prevents that ally from taking damage instead of the captain."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +18 (`pf2:1`) (magical, versatile p), **Damage** 1d8+11 slashing"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +12 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Shielded Advance"
    desc: "`pf2:1` **Requirements** The captain of the guard has their shield raised <br>  <br> **Effect** The captain of the guard presses forward, using their shield to push back foes. The captain Strides and Shoves, in either order. The multiple attack penalty doesn't apply to this Shove, though the Shove does count toward the captain's multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The captain of the guard leads a troop of soldiers who serve as security forces for a powerful individual, most often a high-ranking noble or very rich merchant, though this stat block could also represent a lowerranking captain of the guard for the leader of a nation. A formidable opponent in their own right, the captain of the guard skillfully employs their troops to protect the life and health of their ward.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Captain Of The Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
