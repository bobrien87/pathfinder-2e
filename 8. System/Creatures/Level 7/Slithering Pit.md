---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Slithering Pit"
level: "7"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Tremorsense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +10"
abilityMods: ["+7", "-5", "+7", "-5", "+0", "-5"]
abilities_top:
  - name: "Transparent"
    desc: "A slithering pit is so clear it's difficult to spot. A successful DC 30 [[Perception]] check is required to notice a stationary slithering pit, and a creature must be [[Searching]] to attempt this check. <br>  <br> A creature that walks into the pit's space might fall into any active Dimensional Pit."
armorclass:
  - name: AC
    desc: "14 10 from inside the Dimensional Pit; **Fort** +18, **Ref** +6, **Will** +11"
health:
  - name: HP
    desc: "220; **Immunities** acid, bleed, critical hits, precision, unconscious, visual"
abilities_mid:
  - name: "Breach Vulnerability"
    desc: "Ingesting an extradimensional space like that found in a Spacious Pouch deals 6d8 force damage to the slithering pit and its occupants. The slithering pit then immediately uses Out You Go."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +18 (`pf2:1`) (reach 10 ft.), **Damage** 2d8+9 bludgeoning plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Dimensional Pit"
    desc: "`pf2:2` The slithering pit opens an extradimensional, 20-foot-deep pit that covers its own space and all adjacent squares unless they're walls or similar blocking terrain. <br>  <br> Any other creature occupying or entering pit spaces must succeed at a DC 22 [[Reflex]] save or fall into the pit, taking damage from the fall (typically 10 bludgeoning damage). Any creature [[Grabbed]] by the slithering pit falls in and is no longer grabbed, even if it was outside the pit squares. <br>  <br> While a Dimensional Pit is open, the slithering pit is [[Immobilized]], can't be forced to move, and can make pseudopod Strikes originating from the walls of the pit. A creature that starts its turn at the bottom of the pit takes 2d6 acid damage. Climbing the walls of the pit requires a DC 22 [[Athletics]] check. <br>  <br> When the slithering pit dies, the Dimensional Pit closes and creatures inside are ejected, with the effects of Out You Go."
  - name: "Flurry of Pods"
    desc: "`pf2:2` The slithering pit makes a single pseudopod Strike against each target within range it doesn't already have [[Grabbed]]. These attacks count toward the slithering pit's multiple attack penalty, but the penalty doesn't increase until after all of these attacks."
  - name: "Out You Go"
    desc: "`pf2:1` The slithering pit closes all pit spaces it created using Dimensional Pit, ejecting all its occupants onto the ground into random free spaces where the pit opened. Each occupant takes 4d6 bludgeoning damage (DC 22 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A slithering pit is a strange, nearly invisible ooze with an extradimensional space for its digestive system, which mimics the appearance of an acid-filled stone pit. It slowly dissolves its captives in stomach acid until they can be digested. A slithering pit can go weeks without feeding, affording it patience.

Thriving in dilapidated areas, the slithering pit takes up position among the plentiful potholes where it can easily pass for just another blemish. It crawls across ramshackle cobblestone streets and damp underground complexes, waiting for unwary prey to stumble by and fall in.

```statblock
creature: "Slithering Pit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
