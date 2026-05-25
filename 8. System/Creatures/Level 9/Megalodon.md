---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Megalodon"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Scent]] (imprecise) 100 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +21, Stealth +19, Survival +16"
abilityMods: ["+8", "+2", "+5", "-4", "+3", "-2"]
abilities_top:
  - name: "Blood Scent"
    desc: "The megaladon can smell blood in the water from up to 1 mile away."
armorclass:
  - name: AC
    desc: "27; **Fort** +21, **Ref** +16, **Will** +17"
health:
  - name: HP
    desc: "180"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +22 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+10 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tail +22 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d8+10 piercing plus [[Push]]"
spellcasting: []
abilities_bot:
  - name: "Breach"
    desc: "`pf2:1` The megalodon Swims up to its swim Speed, then [[Leaps]] vertically out of the water up to 25 feet high, making a Strike against a creature at any point during the jump (this lets it attack a creature within 35 feet of the water's surface or 40 feet with its tail). After the Strike, the megalodon splashes back down into the water."
  - name: "Savage"
    desc: "`pf2:1` **Requirements** The megalodon hit with a jaws Strike on its most recent action this turn. <br>  <br> **Effect** The creature the megalodon hit takes 2d12 slashing damage."
  - name: "Swallow Whole"
    desc: "`pf2:1` Huge, @Damage[(2d8+5)[bludgeoning]], Rupture 20 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Push 15 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Prehistoric sharks of incredible size, strength, and ferocity, megalodons scour waters deep and shallow to sate their considerable hunger. The presence of a megalodon undeniably affects the local aquatic ecosystem.

Sharks of all shapes and sizes have stalked the oceans, largely unchanged, since primordial times. They are efficient, ruthless predators with multiple rows of razor-sharp teeth capable of rending prey in an instant. Their uncanny ability to smell blood in the water means sharks might show up at any scene of aquatic carnage.

```statblock
creature: "Megalodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
