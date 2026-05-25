---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Watch Officer"
level: "3"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +11, Diplomacy +6, Intimidation +9, Society +5, Legal Lore +7"
abilityMods: ["+4", "+1", "+3", "+0", "+1", "+1"]
abilities_top:
  - name: "+1 to Sense Motive"
    desc: ""
armorclass:
  - name: AC
    desc: "19 (21 with shield raised); **Fort** +10, **Ref** +6, **Will** +8"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Air of Authority"
    desc: "10 feet. Creatures in the aura who are the same or lower level than the watch officer take a -2 status penalty to their Will DC against the watch officer's attempts to `act coerce` or `act demoralize` them."
  - name: "Bravery"
    desc: "When the watch officer rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the [[Frightened]] condition, reduce its value by 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +13 (`pf2:1`) (shove), **Damage** 1d8+7 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Sudden Charge"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The watch officer Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against that enemy."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Often leading a small team of lower-ranking guards, watch officers patrol their assigned areas to maintain order and enforce laws. Watch officers get the job done, though their methods aren't always gentle or kind.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Watch Officer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
