---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gancanagh"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +9, Deception +13, Diplomacy +13, Performance +14, Religion +9, Stealth +11"
abilityMods: ["+1", "+5", "+3", "+2", "+1", "+5"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "75; **Weaknesses** cold iron 5, unholy 5"
abilities_mid:
  - name: "Vulnerable to Smoke"
    desc: "A gancanagh's lungs can't tolerate smoke. They take a -2 circumstance penalty to saving throws against effects that create some form of smoke."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Silver Rapier +13 (`pf2:1`) (deadly d10, disarm, finesse, holy, magical), **Damage** 1d6+7 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]]<br>**3rd** [[Heroism]]<br>**2nd** [[Sure Footing]]<br>**1st** [[Charm]] (At Will), [[Heal]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The gancanagh can take on the appearance of any Small or Medium humanoid. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Invigorating Passion"
    desc: "`pf2:2` The gancanagh embraces or kisses a willing creature adjacent to them, infusing that creature with their invigorating passion. For 10 minutes, the creature gains a +1 status bonus to attack rolls and 10 temporary Hit Points. After that time, the target becomes [[Fatigued]] for 10 minutes unless it succeeds at a DC 21 [[Fortitude]] save. <br>  <br> > [!danger] Effect: Invigorating Passion"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gancanaghs are lovers, revelers, and dashing duelists of Elysium. Embodiments of free love, they eagerly throw themselves into courting targets for brief but earnest flings until their quicksilver passions change their desires. They serve Cayden Cailean as well as other bacchanalian deities and empyreal lords of Elysium who understand their desires for love and parties. Gancanaghs hate evil beings that profane the spirit of romance and passion, as such creatures (especially the demonic tempters known as succubi) reinforce stigmas against open and free love. One can give no greater insult to a gancanagh than to mistake them for such a creature, and more than one hotheaded gancanagh has challenged a misinformed champion to a duel over such a slight. While they enjoy drinking and carousing, gancanaghs can't stand smoke. Nonetheless, many gancanaghs carry whimsical-looking smoking pipes because they think it makes them look dapper. They cherish their silver flutes, for they enjoy the beauty of flutes' music and its ability to sway the heart.

The majority of gancanaghs present themselves as male, but the concept of gender to a creature like a gancanagh, who can change their shape freely, is much more fluid and open to interpretation than for many mortals. Gancanaghs enjoy using this flexibility to confront and test mortals' convictions when faced with fear or prejudice, but when encountering mortals who themselves are open-minded about sexuality or gender identity, they can become lifelong allies. For those who are persecuted for such reasons, gancanaghs are tireless defenders and eager supporters, quick to provide safety and to punish those who would attempt to impose narrower beliefs upon a world that deserves more diversity than it often gets. If possible, a gancanagh seeks to educate and redeem those who hold destructive beliefs or prejudices, resorting to combat only to defend themself or an endangered mortal, or when no other option seems tenable—yet even then, they fight with sadness.

Azatas are manifestations of freedom and unrestrained joy—kindly celestials with a penchant for curious exploration, spontaneous revelry, and whimsical quests. Born of good dreams and heartfelt wishes for a better world, they reside in the untamable wilds of Elysium. Azatas are passionate and mercurial, as beautiful and bright as a child's fantasy, but also fiercely loyal to those they hold dear. They act quickly and directly against fiendish and foul influences, but they tend to avoid guiding mortal affairs otherwise, allowing people to choose their own destiny without the meddling of otherworldly forces.

Azatas reject the dual chains of both duty and tyranny, but also the heavy chains of despair that reality so often inflicts upon those who live in it. This can give them a dubious reputation with other celestials, who consider azatas to be flighty and unreliable, but azatas know that unrelenting self-sacrifice can be just as destructive to the soul as evil. Azatas refuse to compromise the beauty of the world with such banality, instead living without regret and savoring every triumph and agony they encounter upon the way.

```statblock
creature: "Gancanagh"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
