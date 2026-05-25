---
type: creature
group: ["Aberration", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Argorth"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aberration"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Bloodsense]] (precise) 120 feet, [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +23"
abilityMods: ["+7", "+3", "+5", "-5", "+1", "-1"]
abilities_top:
  - name: "Bloodsense"
    desc: "The argorth can detect any creature that has a heartbeat, such as most humanoids, or any creature that's consumed blood within 1 week, such as a vampire."
armorclass:
  - name: AC
    desc: "30; **Fort** +24, **Ref** +21, **Will** +18"
health:
  - name: HP
    desc: "200; **Immunities** visual; **Resistances** acid 10, cold 10"
abilities_mid:
  - name: "Death Slam"
    desc: "`pf2:r` **Trigger** The argorth is reduced to 0 Hit Points <br>  <br> **Effect** Before it's knocked out, the argorth makes a tail Strike against a random creature within reach."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+13 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d8+13 bludgeoning plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` The argorth can only Constrict creatures [[Grabbed]] by its tail. <br>  <br> @Damage[(2d8+7)[bludgeoning]], DC 27 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Ground Pound"
    desc: "`pf2:2` The argorth rears up its massive bulk and slams it downward with incredible force. Each creature in a @Template[type:emanation|distance:10] takes @Damage[5d8[bludgeoning]|options:area-damage] damage (DC 27 [[Reflex]] save). A creature who critically fails this save is also knocked [[Prone]]."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d8+7)[bludgeoning]], Rupture 24 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Unnatural Shriek"
    desc: "`pf2:2` The argorth emits a terrible howl not of the mortal world. Each non-aberration creature within 120 feet must attempt a DC 30 [[Will]] save. Regardless of the result, a creature is temporarily immune to the argorth's Unnatural Shriek for 24 hours. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is stupefed 1 for 1 minute and [[Frightened]] 2. <br> - **Critical Failure** The creature is stupefed 2 for 1 minute and [[Frightened]] 3."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An argorth is a huge, worm-like creature with three massive spiked mandibles surrounding its gnashing maw. It moves atop a series of hook-shaped bones protruding from its underbelly, supplemented by an occasional push with the back half of its 30-foot length. The mindless, eyeless argorth knows nothing but rage and destruction, making it more like a natural disaster than any known beast of the natural world.

Argorths are the incomprehensible spawn of dibrasgorths. They slough off fully formed from the parent creature's mass of tentacles, though scholars and sages don't know exactly when or why this process occurs. The study of such aberrations is hindered by their incredibly violent nature; not many can escape the fury of an argorth, let alone a molting dibrasgorth. Once birthed, an argorth immediately engages in the wanton destruction of everything around it. Though it has no eyes, both its ability to instinctively sense creatures with pumping blood as well as the thousands of tiny coarse hairs covering its body allowing it to "smell" the air around it ensure that nothing escapes its rampage.

```statblock
creature: "Argorth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
