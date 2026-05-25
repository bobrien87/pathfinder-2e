---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Anaconda"
level: "8"
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
    desc: "+17; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +21, Stealth +15, Survival +15"
abilityMods: ["+7", "+3", "+6", "-4", "+3", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +20, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "175"
abilities_mid:
  - name: "Tighten Coils"
    desc: "`pf2:r` **Trigger** A creature [[Grabbed]] or [[Restrained]] by the giant anaconda attempts to [[Escape]]. <br>  <br> **Effect** The DC of the Escape check is increased by 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +19 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+7 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +19 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d8+7 bludgeoning plus [[Push]]"
spellcasting: []
abilities_bot:
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(1d10+7)[bludgeoning]], DC 26 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
  - name: "Slither"
    desc: "`pf2:1` The giant anaconda Strides, Climbs, or Swims up to half its Speed, pulling any creatures it has [[Grabbed]] with it."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(1d10+7)[bludgeoning]], Rupture 21 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Wrap in Coils"
    desc: "`pf2:1` **Requirements** A Large or smaller creature is [[Grabbed]] or [[Restrained]] in the giant anaconda's jaws. <br>  <br> **Effect** The giant anaconda moves the creature into its coils, freeing its jaws to make attacks, then uses Greater Constrict against the creature. The giant anaconda's coils can hold as many creatures as will fit in its space."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Push 10 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The monstrous giant anaconda is a constrictor snake capable of swallowing whole creatures as big as horses—to say nothing of their riders. Although novice bushwhackers watch out for snakes that might drop on them from the jungle canopy above, giant anacondas are most commonly encountered in ponds and rivers, where they feed on prey including manatees and capybaras. This hunting tactic allows anacondas to drown their prey while constricting it, reducing the chance of injuries while hunting. Despite lurid and sensational stories spread by adventurers, these snakes rarely attack humanoids.

Snakes come in an array of forms, from jungle-dwelling constrictors that wrap around their prey to venomous vipers with deadly bites. Regardless, all snakes consume their prey whole by unhinging their jaws and using powerful muscles to move the food down their throats and into their stomachs.

```statblock
creature: "Giant Anaconda"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
