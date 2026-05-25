---
type: creature
group: ["Fungus", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Terotricus"
level: "19"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Fungus"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+31; [[Darkvision]], [[Tremorsense]] (imprecise) 120 feet"
languages: "Chthonian, Elven, Fey"
skills:
  - name: Skills
    desc: "Athletics +37, Deception +32, Intimidation +35, Nature +31, Survival +31"
abilityMods: ["+10", "+5", "+9", "-1", "+6", "+5"]
abilities_top:
  - name: "Spore Blight"
    desc: "Plants and fungi are immune. <br>  <br> **Saving Throw** DC 40 [[Fortitude]] save <br>  <br> **Stage 1** [[Enfeebled]] 2 (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 4 and [[Slowed]] 1 (1 day) <br>  <br> **Stage 3** [[Controlled]] by the terotricus (as [[Dominate]]; 5d8 days) <br>  <br> **Stage 4** dead"
  - name: "Sticky Spores"
    desc: "A creature hit by a terotricus's spores takes a –10-foot status penalty to all its Speeds for 1 minute. If the Strike was a critical hit, the creature is also [[Immobilized]] until it Escapes. <br>  <br> > [!danger] Effect: Sticky Spores"
armorclass:
  - name: AC
    desc: "42; **Fort** +34, **Ref** +28, **Will** +33"
health:
  - name: HP
    desc: "370; regeneration 25 (deactivated by cold); **Immunities** controlled, disease, paralyzed, sleep; **Weaknesses** cold 15, cold iron 15, holy 15, slashing 10; **Resistances** fire 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 25 (Deactivated by Cold)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Spore Cloud"
    desc: "30 feet. <br>  <br> A creature entering the aura or starting its turn there is exposed to spore blight."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Improved Push 20 feet"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +37 (`pf2:1`) (magical, reach 20 ft., unarmed, unholy), **Damage** 4d10+18 bludgeoning plus 2d6 spirit plus [[Improved Grab]] plus [[Improved Push]]"
  - name: "Ranged strike"
    desc: "Spores +37 (`pf2:1`) (brutal, magical, unholy, range 80 ft.), **Damage** 4d8+8 poison plus 2d6 spirit plus [[Spore Blight]] plus [[Sticky Spores]]"
spellcasting: []
abilities_bot:
  - name: "Infest Environs"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Requirements** The terotricus is in a swamp or forested area <br>  <br> **Effect** The terotricus drains nutrients from nearby trees and undergrowth while simultaneously infesting them with fungal growth. All non-magical plant life (though not plant creatures) within a @Template[emanation|distance:60] withers and sprouts foul mold and slimy mushrooms, removing any cover and concealment provided by trees and undergrowth. In addition, the terotricus regains 200 Hit Points (this is a healing vitality effect)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The legendary terotricus is a massive slime mold that hails from the Outer Rifts. Its collective consciousness encapsulates entire regions, spreading as far as its ever-growing cloud of spores will take it. Once it has seeped into the Universe from the Rifts, a terotricus's agenda is to feed on all living creatures, infecting them with its spores, and its presence can spell doom for any in its way.

Terotricuses move by rapidly expanding and contracting their slimy "bodies," which are capable of burrowing through soil, gliding across water, and scrabbling up steep slopes. These behemoths of rot don't need to travel to see their plans come to fruition, though; their spores easily latch onto demons and other denizens of the Outer Rifts, who in turn bring this blight to the Universe when the fiends are summoned.

When a terotricus infects a creature with its spores, web-like fungal growths start appearing on the victim's skin until they cover the entire body, at which point the victim's mind is also subdued and bent to the terotricus's will. The terotricus's favored victims include animals, elves, and fey, though it is happy to infect any creature it can catch. Cults of Treerazer occasionally attempt to make contact with a terotricus, but such acts almost always simply result in a new sect of spore-blighted servants.

```statblock
creature: "Terotricus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
