---
type: creature
group: ["Dwarf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dwarf General"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common, Dwarven"
skills:
  - name: Skills
    desc: "Athletics +19, Diplomacy +12, Intimidation +14, Medicine +15, Society +13, Survival +15, Warfare Lore +15"
abilityMods: ["+5", "+0", "+4", "+2", "+2", "+1"]
abilities_top:
  - name: "Hammer Critical Specialization"
    desc: "When the general critically hits with a hammer, the target of the critical hit is knocked [[Prone]] unless it succeeds at a DC 26 [[Fortitude]] save."
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "Opening Orders"
    desc: "`pf2:0` **Trigger** The dwarf general rolls initiative and can see at least one enemy <br>  <br> **Effect** The general unleashes a command to ready for combat. Each ally within 120 feet that can hear the general can either Raise a Shield or Step as a free action when it rolls initiative."
  - name: "Dwarven Doughtiness"
    desc: "Dwarves are often calm and collected in the face of imminent danger. At the end of the general's turn, reduce its [[Frightened]] condition by 2 instead of 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` The dwarf general gains an additional reaction at the beginning of each of their turns that they can use only for a Reactive Strike. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Clan Dagger +19 (`pf2:1`) (agile, parry, versatile b), **Damage** 1d4+11 piercing"
  - name: "Melee strike"
    desc: "Warhammer +20 (`pf2:1`) (magical, shove), **Damage** 2d8+11 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Arbalest +15 (`pf2:1`) (backstabber, reload 1, range 110 ft.), **Damage** 1d10+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Advancing Orders"
    desc: "`pf2:1` The dwarf general issues a command to push forward on the battlefield. Each ally who hears and understands this command becomes [[Quickened]] until the end of its next turn but can use the extra action only to Step or Stride."
  - name: "Sudden Charge"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The dwarf general Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against that enemy."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Dwarven generals embody pride in knowledge and tactical acumen, using their understanding of warfare and battlefield strategy to coordinate their subordinates into optimal locations. They also remain ready to enter combat at a moment's notice and bring a fight to an enemy themselves.

From the dwarven perspective, most things in life are best done correctly, and that means taking one's time. Dwarves are a focused and intentional people, taking years or even decades to ply their trades, doing their best to make every detail perfect. The patience and dedication required for such tasks pays off, and many dwarves become experts in their respective field, trade, or area of focus. Many dwarves uphold traditions, and since dwarven origins trace back to underground life, many still hone skills focused on life underground.

```statblock
creature: "Dwarf General"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
