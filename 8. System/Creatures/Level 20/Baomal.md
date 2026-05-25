---
type: creature
group: ["Aberration", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Baomal"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+34; [[Darkvision]], [[Scent]] (imprecise) 80 feet"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Athletics +41, Stealth +31, Survival +37"
abilityMods: ["+10", "+2", "+8", "-3", "+6", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "46 all-around vision; **Fort** +36, **Ref** +30, **Will** +34"
health:
  - name: HP
    desc: "315; **Resistances** physical 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Doubled Reaction"
    desc: "A baomal gains an extra reaction each round that it can use only to make a Reactive Strike. It must use a different head for each one it attempts, and it can't make more than one Attack of Opportunity for the same triggering action."
  - name: "Psychic Static Aura"
    desc: "120 feet. All creatures, except aberrations, that begin their turn in the area take @Damage[5d6[mental]|options:area-damage] damage."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Two Heads"
    desc: "Any ability that would sever a baomal's head (such as a critical hit with a [[Vorpal]] weapon) severs one head at random. Losing one head doesn't kill a baomal, but it does prevent the baomal from making Strikes with the lost head and from using Double Reaction or Two-Headed Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (reach 20 ft., unarmed), **Damage** 4d12+18 piercing plus [[Improved Grab]]"
  - name: "Ranged strike"
    desc: "Tsunami Jet +38 (`pf2:1`) (brutal), **Damage** 4d10+18 bludgeoning plus [[Push]]"
spellcasting: []
abilities_bot:
  - name: "Breath of the Sea"
    desc: "`pf2:1` A baomal can inhale tremendous amounts of water, drawing everything in the sea nearby closer. All creatures and objects in the water within @Template[emanation|distance:60]{60 feet} of the baomal (including ships) are pulled toward it. Creatures must succeed at a DC 42 [[Athletics]] check or be pulled up to 20 feet toward the baomal (40 feet on a critical failure). For ships, use the captain's Sailing Lore in place of Athletics. Unattended objects are automatically pulled."
  - name: "Shell Rake"
    desc: "`pf2:1` The baomal Swims or Strides alongside a creature or the hull of a vessel, dealing damage with the strong spikes on its shell. Each creature or ship the baomal is adjacent to at any point during its movement takes @Damage[(6d6+10)[slashing],(6d6+10)[piercing]]{6d6+10 slashing and piercing damage} (DC 42 [[Reflex]] save). Against vessels, Shell Rake ignores the first 5 Hardness and creates an explosion of splinters that deals @Damage[(3d6+5)[untyped]|options:area-damage] damage to every creature within @Template[burst|distance:10]{10 feet} of the deck's edge (DC 42 [[Reflex]] save)."
  - name: "Two-Headed Strike"
    desc: "`pf2:2` The baomal makes a Strike with each set of jaws, each against a different creature. These Strikes count as one attack for the baomal's multiple attack penalty, and the penalty doesn't increase until after both attacks."
  - name: "Push 40 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Few sea monsters are as dreaded and feared as the two-headed baomal. These massive predatory beasts typically dwell in the deepest waters and compete with krakens and other monsters for food. They feed on whales and other large sea creatures, sometimes following them to the water's surface. Near the surface, baomals that encounter ships quickly learn that they contain a variety of tasty morsels. The creatures use their devastating spikes to rip open the ships' hulls, then leisurely feed on the helpless sailors.

```statblock
creature: "Baomal"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
