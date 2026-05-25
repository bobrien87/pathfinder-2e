---
type: creature
group: ["Aquatic", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Demontangle"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aquatic"
trait_02: "Ooze"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15"
abilityMods: ["+6", "-5", "+5", "-5", "+0", "-5"]
abilities_top:
  - name: "Nauseating Slap"
    desc: "A living creature struck by a demontangle's tendril must attempt a DC 19 [[Fortitude]] save. On a failure, the creature becomes [[Sickened]] 1. If the creature is already sickened, the condition value increases by 1, to a maximum of sickened 4. <br>  <br> Once a creature succeeds at its saving throw, it is temporarily immune for 24 hours."
  - name: "Saturated"
    desc: "A demontangle can survive for 1 hour out of the water, after which it risks drowning and suffocation."
armorclass:
  - name: AC
    desc: "12; **Fort** +16, **Ref** +6, **Will** +9"
health:
  - name: HP
    desc: "170; **Immunities** critical hits, mental, unconscious; **Weaknesses** bludgeoning 5, cold iron 5, holy 5"
abilities_mid:
  - name: "Stench"
    desc: "30 feet. DC 19 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +15 (`pf2:1`), **Damage** 2d8 + 6 bludgeoning plus [[Grab]] plus [[Nauseating Slap]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+6)[bludgeoning]], DC 22 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Since the Worldwound opened over a century ago, countless demons have been slaughtered on the streets of Domora. Their remains sometimes coalesce into further unholy terrors, among the most gruesome examples of which are a trio of large, quivering tangles of knotted demon tongues. These “demontangles” haunt the city's streets day and night, slithering across the ruins in search of mortals to corrupt, destroy, and consume.

The tide washes ashore all manner of detritus, from harmless seaweed and shells to the rotting corpses of massive aquatic creatures. The globster is often mistaken for such, and this assumption isn't entirely incorrect—these mindless, oozing masses are composed of decaying sea creatures, half-digested and merged into a revolting, reeking heap of blubbery sludge.

Though mindless, globsters are predators that seek out living quarry. They often huddle on the seafloor, where their own fetid mass attracts scavengers who swiftly become the ooze's next meal. When the tides wash these monsters ashore, they simply shift to hunting land-bound prey. Coastal communities usually notice the smell of a washed-up globster long before they see it. Those sent to investigate often mistake a globster for the carcass of a beached whale before discovering the presumed corpse is very much alive and hungry.

Sages once believed globsters were undead, undulating wads of rotting flesh driven to feed, but though mindless, they are very much alive. They are attracted to waterside refuse dumps and floating garbage scows and are dimly aware enough to congregate where food is plentiful.

Since they consist of so much blubber and oily tissue, globsters can be collected for lamp oil, grease, cooking fat, and more. The goo that remains when they decompose works for this purpose, if one can stand the smell. The firmer fat deteriorates quickly, but many an impromptu goblin beach barbecue has deep-fried slabs of it as a delicacy.

Globsters consume living creatures but digest only a portion of them. The undigested dross accumulates within the globster as it becomes more and more bloated. They carry this fetid mass within their squelching bodies until instinct or injury provokes them to vomit forth a new globster to help devour everything nearby. A globster with enough dross to create a new globster automatically does so as a free action triggered upon taking damage. Treat any encounter with such a globster as though it were against two level 5 creatures, instead of just one. As far as scholars know, this is the only way these creatures can create more of their kind.

```statblock
creature: "Demontangle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
