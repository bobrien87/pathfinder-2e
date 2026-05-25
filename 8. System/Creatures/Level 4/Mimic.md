---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mimic"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +12, Deception +8, Dwelling Lore (applies only to the dungeon they live in) +10"
abilityMods: ["+4", "+1", "+3", "+0", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +11, **Ref** +9, **Will** +9"
health:
  - name: HP
    desc: "75"
abilities_mid:
  - name: "Object Lesson"
    desc: "`pf2:r` **Trigger** A creature touches or physically interacts with the mimic while the mimic is transformed using Mimic Object <br>  <br> **Effect** The mimic makes a jaws Strike against the triggering creature. If initiative hasn't yet been rolled, the mimic then rolls initiative. Object Lesson can't be used again until the mimic escapes and takes on a new disguise."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`), **Damage** 2d8+4 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Pseudopod +14 (`pf2:1`) (agile, reach 10 ft.), **Damage** 1d8+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Mimic Object"
    desc: "`pf2:1` The mimic assumes the shape of any Medium object. This doesn't change the mimic's texture or overall size but can alter their coloration and visual appearance. They have an automatic result of 28 on Deception checks and DCs to pass as the object that they're mimicking."
  - name: "Mobile Morph"
    desc: "`pf2:1` The mimic transforms part of their body into climbing claws, wings, or paddles. Until the end of their turn, they gain a climb, fly, or swim Speed of 40 feet. This speed is halved if the mimic has a creature swallowed. If they're in the air at the end of their turn, they fall as normal."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, 2d8 acid, Rupture 13 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Thought to be the result of a failed experiment meant to animate furniture or possibly a sinister alghollthu creation, mimics are clever monsters that can take the form of common manufactured objects. While rumored to prefer to be doors, any object that another creature will eventually interact with is an acceptable form to take. Mimics are ambush predators and voracious eaters, surprising their prey through their uncanny ability to imitate the form of ordinary furniture and other common miscellany. They remain disguised until unsuspecting adventurers happen by, then they lash out in ambush.

Mimics possess complex alien minds, and while often cruel and self-serving, they also enjoy conversation with their prey from time to time. For unknown reasons, they're especially interested in humanoids, and tales tell of the occasional mimic who has even formed a partnership with them for larger, shared goals. Mimics have a strong dislike for others of their kind and tend to live alone. Mimics can remain in their alternate form for an extremely long period of time, sometimes remaining disguised in a dungeon chamber for decades. Regardless of how long they wait, mimics remain vigilant and alert, ever ready to ensnare an unsuspecting victim.

```statblock
creature: "Mimic"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
