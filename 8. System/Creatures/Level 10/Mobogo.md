---
type: creature
group: ["Amphibious", "Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mobogo"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Boggard (speak with animals)"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +23, Nature +21, Stealth +19"
abilityMods: ["+7", "+5", "+6", "-2", "+5", "+7"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Swamp Stride"
    desc: "A mobogo ignores difficult terrain caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "A creature hit by the mobogo's tongue becomes [[Grabbed]] by the mobogo. The creature isn't [[Immobilized]], but it can't move beyond the reach of the mobogo's tongue. <br>  <br> A creature can sever the tongue with a Strike against AC 27 that deals at least 10 slashing damage. This deals no damage to the mobogo but prevents it from using its tongue Strike until it regrows its tongue, which takes 1 round. <br>  <br> The mobogo can move without ending the Grab as long as the creature remains within the tongue's reach."
armorclass:
  - name: AC
    desc: "29; **Fort** +22, **Ref** +17, **Will** +19"
health:
  - name: HP
    desc: "160; regeneration 30 (deactivated by acid, cold, or fire)"
abilities_mid:
  - name: "Regeneration 30 (Deactivated by Acid, Cold, or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+13 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tongue +23 (`pf2:1`) (agile, reach 30 ft.), **Damage** 2d6+13 bludgeoning plus [[Tongue Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27, attack +19<br>**5th** [[Control Water]]<br>**2nd** [[Entangling Flora]], [[Mist]], [[Noise Blast]] (At Will), [[Speak with Animals]] (Constant)<br>**1st** [[Create Water]] (At Will), [[Vanishing Tracks]] (Constant)"
abilities_bot:
  - name: "Song of the Swamp"
    desc: "`pf2:1` **Frequency** once per 10 minutes <br>  <br> **Effect** The mobogo unleashes a booming croak. All boggards and mobogos within @Template[emanation|distance:50]{50 feet} gain a +2 status bonus to damage rolls and saves against fear for 1 round. Other creatures in the area of effect must attempt a DC 27 [[Will]] save. <br> - **Success** The creature is unaffected and is temporarily immune for 24 hours. <br> - **Failure** The creature is [[Slowed]] 1 for 1d4 rounds. <br> - **Critical Failure** The creature is [[Slowed]] 2 for 1d4 rounds. <br>  <br> > [!danger] Effect: Song of the Swamp"
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d12+6)[bludgeoning]], Rupture 19 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Tongue Reposition"
    desc: "`pf2:1` When a mobogo successfully Repositions a creature [[Grabbed]] by their tongue, they increase the distance they can move that creature by 10 feet (a total of 15 feet on a success or 20 feet on a critical success); the creature must remain within the tongue's reach. Alternatively, the mobogo can transfer the grabbed creature to being grabbed by the mobogo's jaws."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Mobogos are massive, swamp-dwelling monstrosities that combine the worst aspects of giant toads and evil dragons. Lazy, cruel, and greedy, these vile creatures make their lairs in the most ancient and primordial swamps. The boggards who call such places home worship mobogos as living demigods, regularly bringing sacrifices of food and valuables lest they become the next victims of the mobogos' boundless appetites.

```statblock
creature: "Mobogo"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
