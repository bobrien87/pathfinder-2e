---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spinosaurus"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +23"
abilityMods: ["+8", "+4", "+6", "-4", "+2", "+1"]
abilities_top:
  - name: "Deep Breath"
    desc: "A spinosaurus can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "30; **Fort** +23, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "200"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bite +23 (`pf2:1`) (deadly d12, reach 20 ft.), **Damage** 2d12+14 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 2d8+14 slashing"
spellcasting: []
abilities_bot:
  - name: "Rip and Tear"
    desc: "`pf2:1` **Requirements** The spinosaurus has a creature [[Grabbed]] or [[Restrained]] in its jaws <br>  <br> **Effect** The spinosaurus reaches up and slashes with its claws at the creature it has grabbed, dealing 4d8 slashing damage (DC 30 [[Reflex]] save). A creature who fails this save also takes 1d6 persistent,bleed damage."
  - name: "Staggering Sail"
    desc: "`pf2:2` **Requirements** The spinosaurus is swimming on the surface of water <br>  <br> **Effect** With a powerful lunge to the side, the spinosaurus uses its sail to slap the surface of the water, creating a crushing wave of water that deals @Damage[6d6[bludgeoning]|options:area-damage] damage in a @Template[cone|distance:30]. Each creature in the water in the area must attempt a DC 30 [[Reflex]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and is [[Slowed]] 1 until the end of its next turn. <br> - **Critical Failure** The creature takes double damage and is [[Stunned]] 3."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, 2d12 bludgeoning damage, Rupture 19 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The spinosaurus is more than just one of the largest carnivorous dinosaurs—it's also one of the most unusual in appearance, with a large, sail-like fin running along its spine. Often quite colorful, this sail allows the spinosaurus to attract mates, aids in swimming, and makes it appear to be even larger than it actually is. A swimming spinosaurus can also use the sail as part of a unique means of staggering prey by slapping the water with it to make a crushing wave. A spinosaurus can measure up to 60 feet in length and weigh 25,000 pounds.

The spinosaurus is equally at home in water as it is on land, and its long, toothy maw is well-adapted for catching swimming prey. Attempts by giants to capture spinosauruses to serve as guardians typically go poorly, for these headstrong dinosaurs do not domesticate well. Their surly attitudes and striking appearances make them better suited for blood sports, and they're popular prizes for those who run arenas specializing in battles that pit gladiators against hungry animals or beasts. These productions are truly feasts of gore for the eyes and command audiences from hundreds of miles around. Of course, an angry dinosaur forced to fight for the amusement of others won't discriminate between potential meals on the battleground and those seated in the surrounding stands, making the seats closest to the edge of the arena possibly part of the show as well.

The spinosaurus's appearance and strength make it attractive to more than just giants and blood sport organizers. Spellcasters who mutate and transform animals into magical guardians have long been intrigued by the spinosaurus's potential. Due to the creature's reputation for violence, these spellcasters face great danger while charming one to bring home. Yet for those intrigued by the creature's hypothetical abilities, such risk is worth it. More so than any other dinosaur, spinosauruses have been subjected to fleshwarping procedures, crossbreeding with monsters, and other magical techniques at the hands of reclusive spellcasters experimenting to enhance the creatures' viability as effective guardians.

```statblock
creature: "Spinosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
