---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Drainberry Bush"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Lifesense]] (precise) 120 feet"
languages: "Aklo, Common, Fey (Can't speak any language, Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +17, Diplomacy +13, Nature +17, Stealth +11"
abilityMods: ["+6", "+2", "+6", "-2", "+4", "+2"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Nature Empathy"
    desc: "The drainberry bush can use Diplomacy to [[Make an Impression]] on and make very simple Requests of animals and plant creatures."
  - name: "Blood Berries"
    desc: "The drainberry bush must drain blood from living creatures for sustenance. This causes clusters of bright red berries to grow among its branches. <br>  <br> Each cluster of berries lasts for 1 day, and a drainberry bush typically has 1d6+3 clusters when encountered. When consumed, a cluster restores @Damage[(2d8+10)[healing]] Hit Points. This effect has the healing, necromancy, and primal traits. <br>  <br> A creature can pluck a cluster of berries with a successful unarmed Strike or Thievery check against the bush's AC."
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +13, **Will** +13"
health:
  - name: HP
    desc: "135; **Weaknesses** fire 10; **Resistances** void 10"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Vine +17 (`pf2:1`) (reach 120 ft.), **Damage** 2d8+10 bludgeoning plus [[Improved Grab]]"
spellcasting: []
abilities_bot:
  - name: "Consume Berries"
    desc: "`pf2:1` The bush draws nourishment from one cluster of blood berries, regaining @Damage[(2d8+10)[healing]] Hit Points. That berry cluster wrinkles and dies."
  - name: "Drain Blood"
    desc: "`pf2:1` **Requirements** The drainberry bush has at least one living creature [[Grabbed]] with one of its vines <br>  <br> **Effect** The bush squeezes all creatures it has grabbed, its hollow thorns piercing flesh and siphoning blood. Each creature must succeed at a DC 25 [[Fortitude]] save or take @Damage[(2d8+10)[piercing]] damage and become [[Drained]] 1 (double damage and [[Drained]] 2 on a critical failure). For every creature damaged this way, a cluster of blood berries immediately grows along the bush's branches."
  - name: "Storm of Vines"
    desc: "`pf2:2` The drainberry bush makes up to four vine Strikes, each against a different target. These attacks count toward the bush's multiple attack penalty, but the multiple attack penalty doesn't increase until after the bush makes all these attacks."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Drainberry bushes are floating bushes that originate from the First World, with long, thorny vines and dense clusters of bright-red berries. Their hollow thorns quickly siphon blood, which is how the carnivorous plants feed, and they rapidly turn consumed blood into fresh batches of delicious berries. They exude a faint white glow that's a result of stored vitality energy.

Drainberry bushes exhibit unusually high intelligence and have an astute sense of value. When creatures attempt to harvest their berries, they typically become insulted by the lack of bartering. Creatures that attempt to converse with drainberry bushes find the plants telepathically convey only short and simple phrases: most commonly, "Money please," "Deal good," "Deal no good," "Want that," (with a gesture toward an item it covets), "Thank you, customer," and if necessary, "No refunds." Though a drainberry bush considers the market value of its berries to be 25 gp, it greatly prefers interesting art objects as payment—even ones of significantly lower value.

```statblock
creature: "Drainberry Bush"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
