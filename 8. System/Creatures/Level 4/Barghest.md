---
type: creature
group: ["Beast", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Barghest"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Goblin, Fey, Jotun"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +11, Diplomacy +9, Intimidation +11, Stealth +10, Survival +12"
abilityMods: ["+5", "+2", "+3", "+2", "+2", "+3"]
abilities_top:
  - name: "Unhealing Wound"
    desc: "A creature damaged by the barghest's claws must succeed at a DC 21 [[Fortitude]] save or be cursed. The cursed creature can't regain Hit Points except via magic until it returns to maximum Hit Points. The creature can attempt a new saving throw against the curse every 24 hours."
armorclass:
  - name: AC
    desc: "20; **Fort** +11, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "50; **Weaknesses** holy 5; **Resistances** physical 5 except cold iron"
abilities_mid:
  - name: "Primal Hunt"
    desc: "`pf2:r` **Trigger** A creature within the barghest's reach takes a move or teleportation action <br>  <br> **Effect** After the triggering action, the barghest can teleport up to 60 feet to a space adjacent to that creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, unarmed, unholy), **Damage** 2d6+5 slashing plus [[Unhealing Wound]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**2nd** [[Invisibility]], [[Mist]]<br>**1st** [[Figment]], [[Light]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The barghest takes on the shape of a humanoid, a dog, or its true form. Their size changes to match the new form. When the barghest is a humanoid, their claw Strike deals bludgeoning damage and they lose their jaws Strike. When the barghest is a dog, their Speed changes to 35 feet. Each individual barghest has only one humanoid form and one dog form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Barghests are canine beasts that take great joy in the hunt, often lurking near humanoid settlements to find prey that can provide a suitable challenge. Even in the deepest wilderness, barghests choose the most clever or difficult prey, searching endlessly for challenges like giants, nymphs, and unicorns.

More than victory or even the possibility of a meal at the end, barghests enjoy the thrill of the chase and the fear they create within their prey. Particularly terrified targets of a hunting barghest might even be allowed to escape, spreading the terror and enticing hunters who can become the barghest's next victims. A handful of barghests resort to learning magical methods of causing fear directly, though they find such fear hollow and unsatisfying.

Although they rarely tolerate the competition of another barghest's presence, these hunters will happily work with anyone who helps them find prey to torment and kill. This often involves enforcing the will of hags or particularly cruel fey, but a bored barghest might also force a family of weaker humanoids to work as scouts and bait.

Typical barghests often make use of their shapechanging abilities to hide in plain sight, only taking their true forms to frighten their prey and exult in the hunt. However, they are often still exposed by their trail of victims or the curiously unhealing wounds they inflict, even in humanoid form. Tales of powerful barghests with invisible heads are sometimes told in remote and dwindling villages. These barghests generally dispense with hiding as a humanoid or dog, instead terrifying entire communities and openly hunting increasingly dangerous prey. Some also extend this pride to their intellect, insisting on matching wits with their prey or even with those who believe they're hunting the barghest.

```statblock
creature: "Barghest"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
