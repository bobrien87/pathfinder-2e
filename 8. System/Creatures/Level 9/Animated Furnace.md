---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Furnace"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18"
abilityMods: ["+7", "-2", "+6", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "30 (26 when broken); construct armor; **Fort** +21, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "135"
abilities_mid:
  - name: "Construct Armor (Hardness 10)"
    desc: "Like normal objects, an animated furnace has Hardness. This Hardness reduces any damage the furnace takes by an amount equal to the Hardness. Once an animated furnace is reduced to fewer than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 26."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Door +21 (`pf2:1`) (magical), **Damage** 2d12+9 bludgeoning plus 1d8 fire plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Fan the Flames"
    desc: "`pf2:2` The animated furnace opens its door and fans its flames in a @Template[cone|distance:30] that deals @Damage[5d6[fire]|options:area-damage] damage (DC 28 [[Reflex]] save)."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d8+9)[fire]], Rupture 15 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This huge forge or oven is animated to protect a workspace or kitchen, travel alongside its owner, or both.

Many animated objects have useful functions but become dangers when uncontrolled.

```statblock
creature: "Animated Furnace"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
