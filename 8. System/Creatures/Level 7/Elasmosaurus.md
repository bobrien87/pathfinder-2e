---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elasmosaurus"
level: "7"
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
    desc: "+16; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +17"
abilityMods: ["+6", "+4", "+6", "-4", "+5", "-1"]
abilities_top:
  - name: "Deep Breath"
    desc: "The elasmosaurus can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +13, **Will** +16"
health:
  - name: HP
    desc: "125"
abilities_mid:
  - name: "Long Neck"
    desc: "An elasmosaurus's long neck allows it to interact with the surface while its body remains submerged underwater. While submerged no deeper than 15 feet underwater, an elasmosaurus can still stick its head up to breathe. An elasmosaurus gains cover against attacks made against creatures that are above the water's surface while it is underwater, even if its head is above the surface."
  - name: "Reactive Strike (Jaws Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (reach 15 ft.), **Damage** 2d12+10 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Paddle +16 (`pf2:1`), **Damage** 2d6+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Drag Below"
    desc: "`pf2:1` The elasmosaurus attempts an Athletics check against a [[Grabbed]] foe's Fortitude DC. If the elasmosaurus succeeds, the foe is forcibly moved 5 feet toward the elasmosaurus's body. If the elasmosaurus critically succeeds, the foe is moved 10 feet toward the elasmosaurus's body."
  - name: "Thrashing Retreat"
    desc: "`pf2:2` A swimming elasmosaurus thrashes the area around it as it attempts to flee. It makes two paddle Strikes, each of which must be against separate targets, and each of which takes the normal multiple attack penalty. It then Swims up to its swim Speed. This Swim does not trigger reactions based on movement."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Elasmosauruses are long-necked, primeval reptiles that dwell in deep oceans and seas. Although not truly a dinosaur, elasmosauruses are often found in similar locations and are similarly titanic creatures. Keeping their massive bodies underwater, elasmosauruses use their long necks to catch prey and snorkel air to their massive lungs while remaining mostly hidden from the surface above. An elasmosaurus is 30 feet long and weighs 6,000 pounds.

As rare and reclusive as they are, elasmosauruses are sometimes mistaken for even rarer creatures called water orms, legendary aquatic denizens of remote lakes known for their elusiveness and craftiness. Whereas elasmosauruses are mundane creatures of animalistic intelligence, water orms are magical beings with near-humanoid intelligence and a curious fascination with mortals, and they seem to delight in confounding onlookers. As a result, it's theorized that a typical water orm is more than happy to lead a group of spectators to a lost elasmosaurus, both to throw its pursuers off its tail and for the hilarity that will inevitably ensue.

While elasmosauruses are often found in lost worlds and unsettled regions, those who dwell in the oceans of the world do not contain their hunting grounds to specific regions. As a result, it's not unheard of for a wandering specimen to find its way to coastal waters. Those that do often find the ports of small towns or even large cities to be wondrous banquets and are usually hunted down by coastal guards or adventurers. When a wayward elasmosaurus like this finds its way into a city's sewer system or reservoirs, though, it can become the stuff of urban legends.

```statblock
creature: "Elasmosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
