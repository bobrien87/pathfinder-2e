---
type: creature
group: ["Mindless", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Snapping Flytrap"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Mindless"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11, Stealth +10"
abilityMods: ["+2", "+3", "+5", "-5", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "50; **Weaknesses** fire 5; **Resistances** acid 5"
abilities_mid:
  - name: "Quick Capture"
    desc: "`pf2:r` **Trigger** A creature hits or touches the flytrap. <br>  <br> **Effect** The flytrap makes a leaf Strike against the triggering creature. If it hits, the creature is [[Grabbed]] in that leaf."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Leaf +11 (`pf2:1`) (reach 10 ft.), **Damage** 1d8+2 piercing plus 1d6 acid plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Focused Assault"
    desc: "`pf2:2` The flytrap attacks a single target with both its two leaves. The flytrap makes one leaf Strike. On a success, the flytrap deals the damage from one leaf Strike plus an additional 1d8 piercing damage for every leaf beyond the first. On a failure, the flytrap deals the damage from one leaf Strike, but it can't use Improved Grab. It deals no damage on a critical failure. This counts toward the flytrap's multiple attack penalty as a number of attacks equal to the number of leaves the flytrap has."
  - name: "Hungry Flurry"
    desc: "`pf2:2` The flytrap makes two leaf Strikes at a -2 penalty, each against a different target. These attacks count toward the flytrap's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all its attacks."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, @Damage[(1d8+1)[bludgeoning],1d6[acid]], Rupture 5 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Snapping flytraps typically have two sets of tooth-edged leaves, each measuring 3 feet wide, at the end of 10-foot-long stalks.

Flytraps eagerly feed on humanoids, monstrous insects, and larger prey.

```statblock
creature: "Snapping Flytrap"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
