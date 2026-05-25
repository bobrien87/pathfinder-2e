---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cave Worm"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Tremorsense]] (imprecise) 100 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +30"
abilityMods: ["+9", "-1", "+7", "-5", "-1", "-1"]
abilities_top:
  - name: "Cave Worm Venom"
    desc: "**Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 5d6 poison damage and [[Enfeebled]] 2 (1 round) <br>  <br> **Stage 2** 6d6 poison damage, and enfeebled 2 (1 round) <br>  <br> **Stage 3** 8d6 poison damage and enfeebled 2 (1 round)"
  - name: "Regurgitate"
    desc: "The purple worm can violently regurgitate a creature or boulder it has swallowed to make a ranged Strike. The Strike deals bludgeoning damage depending on the size of the projectile: <br>  <br> - Tiny @Damage[(2d6+13)[bludgeoning]]{2d6+13} <br>  <br> - Small @Damage[(3d6+13)[bludgeoning]]{3d6+13} <br>  <br> - Medium @Damage[(4d6+13)[bludgeoning]]{4d6+13} <br>  <br> - Large @Damage[(5d6+13)[bludgeoning]]{5d6+13} <br>  <br> - Huge @Damage[(6d6+13)[bludgeoning]]{6d6+13} <br>  <br> A regurgitated creature takes falling damage from the height of the target or from 20 feet, whichever is greater. <br>  <br> Boulders occupy space in the worm's stomach as a creature of equivalent size, and purple worms often have several boulders swallowed. A purple worm can use a single action to swallow a new boulder."
  - name: "Rock Tunneler"
    desc: "A cave worm can burrow through solid stone at a Speed of 20 feet. It can leave a tunnel if it desires, and it usually does."
armorclass:
  - name: AC
    desc: "32; **Fort** +28, **Ref** +21, **Will** +21"
health:
  - name: HP
    desc: "270"
abilities_mid:
  - name: "Inexorable"
    desc: "The cave worm recovers from the [[Paralyzed]], [[Slowed]], and [[Stunned]] conditions at the end of its turn. It's also immune to penalties to its Speeds and the [[Immobilized]] condition, and it ignores difficult terrain and greater difficult terrain."
  - name: "Slough Skin"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The cave worm would be affected by a condition or adverse effect (such as [[Cursed Metamorphosis]]) <br>  <br> **Effect** The cave worm negates the triggering condition or effect by sloughing an outer layer of its skin. Effects from artifacts, deities, or a similarly powerful source can't be avoided in this way."
  - name: "Fast Swallow"
    desc: "`pf2:r` **Trigger** The cave worm [[Grab|Grabs]] a creature. <br>  <br> **Effect** The worm uses Swallow Whole."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +28 (`pf2:1`) (deadly 2d10, reach 15 ft., unarmed), **Damage** 3d10+15 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Stinger +28 (`pf2:1`) (agile, poison, reach 15 ft.), **Damage** 2d12+15 piercing plus [[Purple Worm Venom]]"
  - name: "Melee strike"
    desc: "Body +26 (`pf2:1`) (reach 15 ft.), **Damage** 1d10+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Regurgitate +26 (`pf2:1`) (brutal, range 60 ft.), **Damage**  plus [[Regurgitate]]"
spellcasting: []
abilities_bot:
  - name: "Swallow Whole"
    desc: "`pf2:1` Huge, @Damage[(3d6+9)[bludgeoning]], Rupture 24 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Thrash"
    desc: "`pf2:2` The worm makes a Strike once against each creature in its reach. It can Strike up to once with its jaws, up to once with its stinger, and any number of times with its body. Each attack counts toward the worm's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all the attacks."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The most common and infamous of the cave worms gives its name to the entire family—a much-feared monster wandering the twisting tunnels of the Darklands that is capable of carving out entire cave systems. Tunnels bored by a cave worm don't always last long after these creature's passage, and areas where they nest are maddening mazes of passageways that lead nowhere, yet navigating the labyrinth to find the worm's central nest often yields amazing treasures left behind by the worm's prior victims.

Cave worms are gigantic scavengers that bore through the depths of the world, eating whatever material they find. Named for their distinctive habitats, these worms are ravenous and display overwhelming destructive capabilities. Cave worms of different types and abilities lurk in the more remote corners of the world—tales speak of arctic worms that dwell within immense glaciers or icebergs and grave worms that burrow through the boneyards of long-forgotten ruins, to name a few.

```statblock
creature: "Cave Worm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
