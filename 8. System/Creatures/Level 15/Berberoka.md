---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Berberoka"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +31, Deception +27, Intimidation +25, Nature +26, Stealth +25, Survival +26"
abilityMods: ["+8", "+4", "+6", "-1", "+3", "+4"]
abilities_top:
  - name: "Deep Breath"
    desc: "A berberoka can hold their breath for 2 hours"
  - name: "Fear of Crabs"
    desc: "If a berberoka sees a crab or crab-like creature, the berberoka must attempt a DC 33 [[Will]] save. They then become immune to the sight of that creature for 10 minutes. <br> - **Critical Success** The berberoka is unaffected. <br> - **Success** The berberoka becomes [[Frightened]] 2. <br> - **Failure** The berberoka gains the [[Fleeing]] condition for 1 round and is [[Frightened]] 4."
  - name: "Consume Lake"
    desc: "The berberoka drinks a prolific amount from an adjacent water source. If the water source is equal to or greater in volume than themself, the berberoka consumes up to 1,500 gallons of water per minute and becomes waterlogged. They can release water at the same rate. While waterlogged, the berberoka can use Spray Water, their size grows to Gargantuan, and their Speed is reduced to 15 feet. <br>  <br> > [!danger] Effect: Waterlogged"
armorclass:
  - name: AC
    desc: "36; **Fort** +29, **Ref** +23, **Will** +24"
health:
  - name: HP
    desc: "310"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +31 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 3d12+16 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Greater Constrict"
    desc: "`pf2:1` @Damage[(2d12+12)[bludgeoning]] damage, DC 33 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC. A creature that fails this save falls [[Unconscious]], and a creature that succeeds is then temporarily immune to falling unconscious from Greater Constrict for 1 minute."
  - name: "Spray Water"
    desc: "`pf2:2` **Requirements** The berberoka is waterlogged. <br>  <br> **Effect** The berberoka sprays a blast of water in a @Template[line|distance:60]. All creatures in the line take @Damage[6d8[bludgeoning]|options:area-damage] damage (DC 35 [[Reflex]] save). On a failed save, a creature is knocked [[Prone]] and pushed back 5 feet (10 feet on a critically failed save)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Berberokas are giant humanoids who live among forests and swamps, where they use their ability to swallow massive amounts of water to drain small ponds and lakes. Creatures who visit their favorite watering hole and find only an empty mud basin become prey for the berberoka, who hides in the brush and overwhelm their prey with a massive torrent of regurgitated water.

A berberoka's mottled backside-which resembles a bundle of local plants, small trees, and large rocks-grants them natural camouflage that allows them to hide in plain sight. Berberokas tend to disguise themselves as rock formations in the center of a dried-up waterbed while they lie in wait for passersby. In the tropical regions where berberokas are most common, locals know to give empty ponds a wide berth, regardless of the enticing fish flopping about. Hungry travelers, on the other hand, might see such bounty as a blessing from the gods, only to be swept up in the berberoka's deadly deluge.

```statblock
creature: "Berberoka"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
