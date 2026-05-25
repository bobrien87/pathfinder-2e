---
type: creature
group: ["Aberration", "Dream"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nightgaunt"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Dream"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Thoughtsense]] (precise) 60 feet"
languages: "Aklo (Can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +13, Stealth +11"
abilityMods: ["+5", "+3", "+2", "-2", "+2", "+0"]
abilities_top:
  - name: "Clutches"
    desc: "A nightgaunt can Fly at full Speed while it has a Medium or smaller creature [[Grabbed]] or [[Restrained]] in its claws, carrying that creature along with it."
  - name: "Tickle"
    desc: "The nightgaunt can use its tail to tickle a foe with horrible efficiency. A creature hit by its tail Strike must attempt a DC 21 [[Fortitude]] save; if the creature is [[Grabbed]] by the nightgaunt, it uses the outcome one degree of success worse than the result it rolled. <br> - **Critical Success** The creature is unaffected and is temporarily immune for 1 minute. <br> - **Success** The creature is overcome with laughter and can't perform reactions for 1 round. <br> - **Failure** As success, and the creature is [[Sickened]] 1. <br> - **Critical Failure** As success, and the creature is [[Sickened]] 2 and can't speak for 1 round."
armorclass:
  - name: AC
    desc: "21 all-around vision; **Fort** +10, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "60; **Resistances** cold 5"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Faceless"
    desc: "The nightgaunt has no face, but it can still see in all directions as if its entire body were an eye. It has no need to breathe, and it is immune to all inhaled toxins and other olfactory effects."
  - name: "Reactive Strike (Tail Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, unarmed), **Damage** 2d6+7 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +12 (`pf2:1`) (agile, reach 10 ft.), **Damage**  plus [[Tickle]]"
spellcasting: []
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nightgaunts lurk in dreams, lying in wait to spirit away the unwary dreamer. Once connected to such a being, the nightgaunt feeds upon the mortal's emotions before abandoning them—often in a place they might never wake from.

A nightgaunt appears as a bony humanoid with inky black skin, batlike wings, a long sinuous tail, and demonic horns atop a head that lacks any face or features. Most nightgaunts have little interest in anything other than sating their hunger for emotions. They find the art of inducing nightmares to be a surefire way to feast, but they're even more adept at tormenting their victims through tickling while carrying them at precarious heights.

Nightgaunts often gather in vast colonies in the Dreamlands, where they entertain each other by sharing emotion memories of their meals through strange caresses. These colonies pose great danger to any adventurer foolish enough to approach.

When conjured forth into other worlds, they serve only grudgingly, often working equally as hard to find a way to escape servitude and feed on their conjurer's emotions as they do on the task they've been compelled to perform.

```statblock
creature: "Nightgaunt"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
