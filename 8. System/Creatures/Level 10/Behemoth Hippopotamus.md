---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Behemoth Hippopotamus"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +23, Stealth +18, Survival +17"
abilityMods: ["+7", "+4", "+7", "-4", "+5", "-2"]
abilities_top:
  - name: "Deep Breath"
    desc: "The behemoth hippopotamus can hold its breath for 1 hour."
armorclass:
  - name: AC
    desc: "29; **Fort** +22, **Ref** +17, **Will** +19"
health:
  - name: HP
    desc: "190"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (deadly d12, reach 10 ft.), **Damage** 2d12+10 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Foot +23 (`pf2:1`), **Damage** 2d8+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "`pf2:1` 40 feet <br>  <br> **Requirements** The monster is hiding in water and a creature that hasn't detected it is within the listed number of feet. <br>  <br> **Effect** The monster moves up to its swim Speed + 10 feet toward the triggering creature, traveling on water and on land. Once the creature is in reach, the monster makes a Strike against it. The creature is [[Off-Guard]] against this Strike."
  - name: "Capsize"
    desc: "`pf2:1` The behemoth hippopotamus tries to capsize an adjacent aquatic vessel of its size or smaller. The behemoth hippopotamus must succeed at an [[Athletics]] check with a DC of 30 (reduced by 5 for each size smaller the vessel is than the hippo) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Double Chomp"
    desc: "`pf2:1` The behemoth hippo makes a jaws Strike targeting two creatures adjacent to each other. Roll the attack and damage once, and apply it to each creature separately. A Double Chomp counts as two attacks for the multiple attack penalty."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, @Damage[(2d12+10)[bludgeoning]] damage, Rupture 26 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, foot, DC 29 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Behemoth hippos are omnivorous and many enjoy the taste of meat.

Hippopotamuses, or hippos for short, are semiaquatic animals that spend most of their time in rivers and lakes, but can thrive on land.

```statblock
creature: "Behemoth Hippopotamus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
