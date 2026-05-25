---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Green Man"
level: "24"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+42; [[Darkvision]]"
languages: "Arboreal, Fey, Wildsong (Green tongue)"
skills:
  - name: Skills
    desc: "Acrobatics +39, Athletics +40, Deception +40, Diplomacy +40, Intimidation +40, Nature +48, Stealth +41, Survival +44"
abilityMods: ["+12", "+9", "+11", "+7", "+10", "+8"]
abilities_top:
  - name: "Green Tongue"
    desc: "A green man can communicate with plants, with the effects of [[Speak with Plants]], and can use Diplomacy to [[Make an Impression]] on plants and [[Request]] things from plants."
  - name: "Plantsense 60 feet"
    desc: "A green man can sense life force via plants. This allows them to observe a living or undead creature's vital essence within 60 feet of the green man, but they can also use this precise sense to observe any living or undead creature within 60 feet of any plant matter within 120 feet of the green man. This allows the green man to see living things through solid plant matter, as well as seeing through other barriers if there are plants on the other side."
  - name: "Embed"
    desc: "The green man's thorns embed themselves into any creature they damage, taking root into the ground. A target damaged by a thorn has its Speeds halved, and it can't Step, Fly, or otherwise leave the ground until the thorn is removed. Removing a thorn requires 3 Interact actions, which don't have to be consecutive. If the creature performing the final action doesn't succeed at a DC 45 [[Medicine]] check as part of that action, the target takes 10d6 piercing damage upon the thorn's removal."
  - name: "Green Grab"
    desc: "A green man can use their [[Improved Grab]] action against a creature of any size."
  - name: "Green Rituals"
    desc: "A green man can perform all their rituals without secondary casters, relying on their own primal ties to the vital essence in spirits of nature. <br>  <br> A green man's [[Awaken Animal]] and [[Primal Call]] rituals work on plants instead of their usual range of choices. <br>  <br> Most green men also know the ritual to create various types of leshys and possibly even magic allowing the creation of arboreals or more powerful plant creatures."
armorclass:
  - name: AC
    desc: "51; **Fort** +43, **Ref** +39, **Will** +42"
health:
  - name: HP
    desc: "525; **Weaknesses** axe vulnerability 20, fire 20; **Resistances** bludgeoning 20, piercing 20"
abilities_mid:
  - name: "Green Caress"
    desc: "60 feet. Living creatures in the area other than plants slowly transform into non-creature plants. The green man can exclude creatures from this effect, but they must be aware of a creature's presence and location to do so. A non-plant creature in the area must attempt a DC 45 [[Fortitude]] save immediately before the start of its turn. <br> - **Critical Success** The creature is unaffected, or if it is slowed by green caress, it reduces its slowed value by 2. <br> - **Success** The creature is unaffected, or if it is slowed by green caress, it reduces its slowed value by 1. <br> - **Failure** The creature becomes [[Slowed]] 1, or if it was already slowed by green caress, increases the slowed value by 1, as their body transforms more and more into a non-creature plant. If the creature ever becomes slowed to the point they have no actions left for their turn, they become an inanimate plant, a condition that can only be reversed by [[Primal Phenomenon]] or similarly powerful magic. <br> - **Critical Failure** As failure, except the creature becomes [[Slowed]] 2 (or increases the condition value by 2)."
  - name: "Root In Place"
    desc: "`pf2:r` **Trigger** A creature within the green man's reach uses a move action or leaves a square during a move action it's using <br>  <br> **Effect** The green man lashes out to hold the foe in place. The green man makes a vine Strike against the triggering creature. If the attack hits, the green man disrupts the action. If the creature was Flying when its action was disrupted, it falls."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Vine +46 (`pf2:1`) (deadly 3d12, versatile p), **Damage** 4d10 + 27 bludgeoning plus [[Absorb Magic]] plus [[Improved Grab]]"
  - name: "Ranged strike"
    desc: "Thorn +43 (`pf2:1`) (fatal d12, reload 0, range 120 ft.), **Damage** 4d8 + 27 piercing plus [[Embed]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 48, attack +40<br>**10th** [[Manifestation]]<br>**7th** [[Energy Aegis]], [[Regenerate]]<br>**6th** [[Truesight]]<br>**5th** [[Nature's Pathway]] (At Will)<br>**4th** [[Fly]], [[Unfettered Movement]]<br>**1st** [[Detect Magic]], [[Heal]], [[Read Aura]]"
abilities_bot:
  - name: "Absorb Magic"
    desc: "`pf2:1` The green man's vines leach away magic and transform it into life essence for the green man. On a successful vine Strike, the green man attempts to counteract one spell active on the target (typically one vexing the green man, or determined randomly if they aren't aware of specific effects), with a counteract rank of 10 and a modifier of +38. <br>  <br> If the effect is counteracted, the green man gains 30 temporary Hit Points that last for 10 minutes."
  - name: "Focus Vines"
    desc: "`pf2:2` The green man focuses all their vines against a single vexing foe, making a single vine Strike. <br>  <br> On a success, the target takes 5d10 additional damage and is affected by Absorb Magic three times. Even on a failure, the target takes the normal effects of a hit with a vine Strike, but on a critical failure, the vines miss completely."
  - name: "Vine Forest"
    desc: "`pf2:2` The green man lashes out with all six vines to attack many opponents. They make up to six vine Strikes, each against a different target; this counts as one attack for their multiple attack penalty, increasing only after all the attacks are made."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Green men are ancient, enigmatic lesser deities of the primeval forests, living embodiments of nature and plantkind. When a forest or other woodland terrain generates enough nature spirits, beings of the same sort of vital essence that embodies leshys or answers the call of a commune with nature, they naturally coalesce together and apotheosize into a green man. Green men aren't concerned with all the multifarious processes of nature like Gozreh or many other nature deities. Instead, they focus nearly all their attention on the plants of their home, only concerning themselves with animals, minerals, and the like insomuch as they affect the plants. Despite their name, green men aren't necessarily male; as creatures of pure natural power, to many of them, the concept of gender holds no meaning, and to those that do, they can be of any gender.

Most green men are neutral and tend to ignore "animals," which to them include sapient creatures such as humans. However, good and evil green men do exist. These individuals are far more likely to attempt to spread their influence far and wide, either for good or ill. Good green men provide succor to all that come within their home, not only to plants, providing wisdom like a nurturing parent. Evil green men, however, allow rare and dangerous plants to thrive in their domains by spreading fear and devastation to all those who might threaten plant life, though they might keep a few animals around to hunt for sport.

```statblock
creature: "Green Man"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
